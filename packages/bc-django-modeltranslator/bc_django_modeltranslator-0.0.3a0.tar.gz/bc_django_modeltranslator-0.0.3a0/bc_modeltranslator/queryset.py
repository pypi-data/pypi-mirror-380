from typing import Any, Dict

from django.db.models import QuerySet
from django.utils.translation import get_language

class BcTranslatedQuerySet(QuerySet):
	def _translate_kwargs(self, kwargs: Dict[str, Any]) -> Dict[str, Any]:
		from .registry import bc_translator
		
		registered_fields = bc_translator.get_registered_fields_for_model(self.model)

		if not registered_fields:
			return kwargs
		
		lang = get_language()
		new_kwargs: Dict[str, Any] = {}

		for key, value in kwargs.items():
			base_field_name = key.split('__')[0]

			if base_field_name in registered_fields:
				new_key = key.replace(base_field_name, f'{base_field_name}_{lang}', 1)
				new_kwargs[new_key] = value

			else:
				new_kwargs[key] = value

		return new_kwargs

	def filter(self, *args: Any, **kwargs: Any) -> "BcTranslatedQuerySet":
		return super().filter(*args, **self._translate_kwargs(kwargs))

	def exclude(self, *args: Any, **kwargs: Any) -> "BcTranslatedQuerySet":
		return super().exclude(*args, **self._translate_kwargs(kwargs))

	def get(self, *args: Any, **kwargs: Any) -> Any:
		return super().get(*args, **self._translate_kwargs(kwargs))

	# def get_or_create(self, defaults=None, **kwargs):
	# 	translated_kwargs = self._translate_kwargs(kwargs)
	# 	return super().get_or_create(defaults=defaults, **translated_kwargs)

	# def update_or_create(self, defaults=None, **kwargs):
	# 	translated_kwargs = self._translate_kwargs(kwargs)
	# 	return super().update_or_create(defaults=defaults, **translated_kwargs)