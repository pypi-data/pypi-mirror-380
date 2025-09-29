def infer():
    # Delegate to internal implementation
    from .infer_cli import cli as _cli
    _cli()


def gradio():
    from .gradio_api import serve as _serve
    _serve()
