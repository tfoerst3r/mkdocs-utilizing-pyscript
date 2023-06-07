---
title: Home
---

<!------------------->
<!----- CHAPTER ----->
<!------------------->
# Testing pyscript

<!-- pyscript routines -->

<py-config src="../pyscript.toml"></py-config>
<py-script src="../mycode/main.py"></py-script>


<!-- PAGE -->
Translate English into Pirate<br>
<input type="text" id="english" placeholder="Type your English in here ..."><br>
[Translate!](#){ .md-button .md-button--primary id="english" style="padding: 0.25rem; text-align: center;" py-click="english_to_pirate()" onclick="clearBox('output')" }

<br>

Input Value<br>
<input type="text" id="showplot" placeholder="Type your int value ..."><br>
[Show it!](#){ .md-button .md-button--primary id="showplot" style="padding: 0.25rem; text-align: center;" py-click="plotter()" onclick="clearBox('output')" }

<div id="output"></div>
<!-- END -->

