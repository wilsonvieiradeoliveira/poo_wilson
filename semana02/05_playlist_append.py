playlist = [
  "Envolver",
  "Tá OK",
  "Houdini",
]
print(playlist[0])
print(playlist[-1])
print(len(playlist))

playlist.append("Nova música")    # adiciona no FINAL
playlist.remove("Tá OK")          # remove pelo VALOR
 
if "Envolver" in playlist:        # o item está na lista?
    print("Essa você já salvou!")
 
# percorrer: o for visita item por item
for musica in playlist:
    print(f"Tocando: {musica}")
