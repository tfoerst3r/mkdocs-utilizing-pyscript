---
title: Pyscript
---

<!-- pyscript routines -->
<div markdown>
<py-config src="../pyscript_level1.toml"></py-config>
<py-script src="../mycode/main.py"></py-script>

<!-- You dare not drink my rum! -->

Translate English into Pirate<br>
<input type="text" id="english" placeholder="Type your English in here ..."><br>
[Translate!](#){ .md-button .md-button--primary id="english" style="padding: 0.25rem; margin-top: 0.5rem; text-align: center;" py-click="english_to_pirate()" onclick="clearBox('output')"  }


Input Value<br>
<input type="text" id="showplot" placeholder="Type your int value ..."><br>
[Show it!](#){ .md-button .md-button--primary id="showplot" style="padding: 0.25rem; text-align: center;" py-click="plotter()" onclick="clearBox('output')" }


<div id="output"></div>
</div>

