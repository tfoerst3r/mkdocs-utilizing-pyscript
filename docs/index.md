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
[Translate!](#){ .md-button .md-button--primary style="padding: 0.25rem; text-align: center;" py-click="translate()" onclick="clearBox('output')" }

<br>

Input Value<br>
<input type="text" id="showgraph" placeholder="Type your int value ..."><br>
[Show it!](#){ .md-button .md-button--primary style="padding: 0.25rem; text-align: center;" py-click="showgraph()" onclick="clearBox('output')" }

<div id="output"></div>
<!-- END -->

