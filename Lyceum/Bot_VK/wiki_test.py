import wikipedia
wikipedia.set_lang("ru")

print(wikipedia.summary("Калуга", sentences=1))