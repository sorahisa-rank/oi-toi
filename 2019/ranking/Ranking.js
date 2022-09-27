if(!window.console){window.console=new Object();}
if(!window.console.log){window.console.log=function(){};}
if(!window.console.info){window.console.info=function(){};}
if(!window.console.warn){window.console.warn=function(){};}
if(!window.console.error){window.console.error=function(){};}
$(document).ready(function(){DataStore.init(function(){HistoryStore.init();UserDetail.init();TimeView.init();TeamSearch.init();Overview.init();Scoreboard.init();});});