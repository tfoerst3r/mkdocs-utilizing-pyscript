---
title: Home
---

<!------------------->
<!----- CHAPTER ----->
<!------------------->
# Testing pyscript

<!-- iframe src="mycode.html" height="700" width="100%" frameBorder="0"></iframe -->


<!-- pyscript routines -->
<div markdown>
<py-config src="./pyscript_level0.toml"></py-config>
<py-script src="./mycode/main.py"></py-script>

<!-- You dare not drink my rum! -->

Translate English into Pirate<br>
<input type="text" id="english" placeholder="Type your English in here ..."> 
[Translate!](#){ .md-button .md-button--primary id="english" style="padding: 0.25rem; margin-left: 0.5rem; text-align: center;" py-click="english_to_pirate()" onclick="clearBox('output')"  }

Input Value<br>
<input type="text" id="showplot" placeholder="Type your int value ..."> 
[Show it!](#){ .md-button .md-button--primary id="showplot" style="padding: 0.25rem; margin-left: 0.5rem; text-align: center;" py-click="plotter()" onclick="clearBox('output')" }


<div id="output"></div>
</div>

