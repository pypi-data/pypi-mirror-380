from datasette import hookimpl

PREACT_OUTFILE = "preact-10.27.2-htm-3.1.1.min.js"

@hookimpl
def extra_template_vars(datasette, template):
    return {
        "datasette_preact_url": datasette.urls.static_plugins(
            "datasette-preact", PREACT_OUTFILE
        )
    }


@hookimpl
def extra_body_script(datasette, view_name):
    return """
// datasette-preact: expose preact URL for dynamic imports
window.datasette = window.datasette || {{}};
datasette.preact = {{
    JAVASCRIPT_URL: '{}',
}};
    """.format(
        datasette.urls.static_plugins("datasette-preact", PREACT_OUTFILE),
    )
