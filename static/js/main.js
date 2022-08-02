jQuery(document).ready(function( $ ) {

	// Простенький скрипт авто-обнавления таблицы
	setTimeout(function run() {
			$('#auto_click').click();
	  setTimeout(run, 600000);
	}, 600000);


});
