from fastapi import FastAPI
from ray import serve

app = FastAPI()


@serve.deployment(ray_actor_options={"num_cpus": 0.25})
@serve.ingress(app)
class RayExampleApp:
    @app.get("/healthz")
    async def healthz(self) -> dict[str, str]:
        return {"status": "success"}

    @app.get("/helloworld")
    async def helloworld(self) -> dict[str, str]:
        return {"message": "helloworld"}


ray_example_app = RayExampleApp.bind()
