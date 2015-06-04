/**
 * Archivo javascript para la vista de inscripciones. Se utiliza una estructura de closures y se define un namespace común (MP) y uno específico (INSCRIPCIONES)
 *
 */


var MP = {};
MP.INSCRIPCIONES = {};

$(document).ready(function () {
    MP.INSCRIPCIONES.inicio();
});


MP.INSCRIPCIONES.inicio = function () {

    $("[id*='id_fecha']").datepicker({
        dateFormat: 'yy-mm-dd',
        changeMonth: true,
        changeYear: true,
        yearRange: "-100:+0"
    });

    $("[id*='id_fecha']").attr("readonly", true);

};