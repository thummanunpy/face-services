# # app/custom_openapi.py
# from fastapi.openapi.utils import get_openapi
# from fastapi import FastAPI
#
# def custom_openapi(app: FastAPI):
#     if app.openapi_schema:
#         return app.openapi_schema
#     openapi_schema = get_openapi(
#         title=app.title,
#         version=app.version,
#         description=app.description,
#         routes=app.routes,
#     )
#     for path in openapi_schema["paths"]:
#         for method in openapi_schema["paths"][path]:
#             openapi_schema["paths"][path][method].pop("summary", None)
#             openapi_schema["paths"][path][method].pop("description", None)
#             openapi_schema["paths"][path][method].pop("operationId", None)
#             openapi_schema["paths"][path][method].pop("tags", None)
#     app.openapi_schema = openapi_schema
#     return app.openapi_schema