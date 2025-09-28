import copy
from typing import Iterable

from django.conf import settings
from django.db.models import Field, base

from .util_model import get_field, BcTransModel
from .dataclasses import BcTranslationField
from .manager import BcTranslatedManager

class InvalidTranslationFieldError(Exception):
	"""Raised when a registered translation field does not exist on the model."""
	pass


class FieldsAggregationMetaClass(type):
	"""
	Metaclass to handle custom inheritance of fields between classes.
	"""

	def __new__(cls, name, bases, attrs):
		if not attrs.get('fields', None):
			return super().__new__(cls, name, bases, attrs)

		attrs['fields'] = list(attrs['fields'])
		
		for base in bases:
			if isinstance(base, FieldsAggregationMetaClass):
				base_fields = getattr(base, 'fields', None)
				if base_fields:
					attrs['fields'].extend(base_fields)

		attrs['fields'] = tuple(attrs['fields'])
		
		return super().__new__(cls, name, bases, attrs)

 
class BcTranslationOptions(metaclass=FieldsAggregationMetaClass):
	pass


class BcTranslation:
	def __init__(self): 
		self._registry = {}
  
	def get_registered_fields_for_model(self, model: base.ModelBase) -> list[str]:
		opts_class = self._registry.get(model)
  
		if not opts_class:
			return []

		registered_fields_objects = getattr(opts_class, 'fields', [])
		
		return [f.field_name for f in registered_fields_objects]

	def validate_registered_fields(self, model: base.ModelBase, opts_class: FieldsAggregationMetaClass) -> bool:
		for bc_field in getattr(opts_class, 'fields', []):
			try:
				model._meta.get_field(bc_field.field_name)
			except Exception:
				raise InvalidTranslationFieldError(
					f"Field '{bc_field.field_name}' does not exist on model '{model.__name__}'. "
					"Check your translation registration."
				)
		return True

	def register(self, model: base.ModelBase, opts_class: FieldsAggregationMetaClass, **options):
		bc_field: BcTranslationField

		if model in self._registry or not self.validate_registered_fields(model, opts_class):
			return

		self._registry[model] = opts_class
		fields: Iterable[BcTranslationField] = getattr(opts_class, 'fields', [])

		for bc_field in fields:
			self.validate_registered_fields(model, bc_field)
			field: Field = model._meta.get_field(bc_field.field_name)
			for lang in settings.LANGUAGES:
				lang_code, _ = lang
				translated_field_name = f"{bc_field.field_name}_{lang_code}"
				if hasattr(model, translated_field_name):
					continue
				new_field = copy.deepcopy(field)
				new_field.attname = translated_field_name
				new_field.name = translated_field_name
				if bc_field.params and lang_code in bc_field.params:
					for attr, value in bc_field.params[lang_code].dict().items():
						setattr(new_field, attr, value)
				model.add_to_class(translated_field_name, new_field)
			field.editable = False
			field.null = True
			field.blank = False

		# Monkey patch
		model._meta._expire_cache()
		model._meta.get_field = get_field.__get__(model._meta, model._meta.__class__)

		if BcTransModel not in model.__bases__:
			model.__bases__ = (*model.__bases__, BcTransModel)

		existing_manager = getattr(model, 'objects', None)
		if not existing_manager:
			return 

		if isinstance(existing_manager, BcTranslatedManager):
			return

		existing_manager_class = existing_manager.__class__

		new_manager_class = type(
			f"Translated{existing_manager_class.__name__}",
			(BcTranslatedManager, existing_manager_class),
			{}
		)
		
		new_manager = new_manager_class()
  
		model.add_to_class('objects', new_manager)


bc_translator = BcTranslation()
