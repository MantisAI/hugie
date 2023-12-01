OPENAPI_CONFIG := https://api.endpoints.huggingface.cloud/api-doc/openapi.json

.DEFAULT_GOAL := update
update: hugie/models_v2.py

.PHONY: hugie/models_v2.py
hugie/models_v2.py:
	touch temp_models.py
	docker run --volume $(PWD):/opt/ \
		koxudaxi/datamodel-code-generator \
		--input-file-type openapi \
		--output-model-type pydantic_v2.BaseModel \
		--enum-field-as-literal all \
		--collapse-root-models \
		--url $(OPENAPI_CONFIG) \
		--output /opt/temp_models.py
	mv temp_models.py hugie/models_v2.py
