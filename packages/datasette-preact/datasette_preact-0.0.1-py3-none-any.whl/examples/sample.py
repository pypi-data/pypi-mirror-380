from datasette import hookimpl, Response

async def test(datasette):
  return Response.html(
    await datasette.render_template("custom-template.html")
  )

@hookimpl
def register_routes():
  return [
    (r"/-/test$", test),
  ]

@hookimpl
def extra_body_script(datasette, view_name):
  if view_name != "index":
        return
  return {
    "module": True,
  "script":"""

  const {render, html, useState} = await import(datasette.preact.JAVASCRIPT_URL);

  function App() {
    const [count, setCount] = useState(0);
    
    return html`<div style="border: 1px dotted gray; padding: 10px; margin: 10px; background-color: #fBd886;">
      <h1>datasette-preact example: extra_body_script</h1>
      <p>This is an example using the extra_body_script hook to add a Preact app to the index page.</p>

      <div>
        <p>Count: ${count}</p>
        <button onClick=${() => setCount(count + 1)}>Increment</button>
      </div>

      <div>
        <p>Go to <a href="/-/test">custom template example</a></p>
      </div>
    </div>`;
  }

  render(html`<${App}/>`, document.querySelector("section.content").appendChild(document.createElement("main")));
  """
  }