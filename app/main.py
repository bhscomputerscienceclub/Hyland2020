import atlastk as Atlas

body = readAsset(body.html)

def acConnect(this, dom, id):
  dom.setLayout("", body)
  dom.focus("input")

def acSubmit(this, dom, id):
  dom.alert("Hello, " + dom.getContent("input") + "!")
  dom.focus("input")

def acClear(this, dom, id):
  if ( dom.confirm("Are you sure?") ):
    dom.setContent("input", "")
  dom.focus("input")

callbacks = {
  "": acConnect,  # The key is the action label for a new connection.
  "Submit": acSubmit,
  "Clear": acClear,
}

Atlas.launch(callbacks)