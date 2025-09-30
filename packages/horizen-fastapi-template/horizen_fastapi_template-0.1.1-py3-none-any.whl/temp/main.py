import horizen_fastapi_template

app = horizen_fastapi_template.general_create_app()
print(f"App version: {horizen_fastapi_template.__version__}")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)