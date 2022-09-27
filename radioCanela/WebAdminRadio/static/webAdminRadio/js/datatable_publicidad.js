//id del comboboxxxx
$("#radioSelect").change(function () {
    var id_emisora = $("#radioSelect option:selected").val();
    getPublicidad(id_emisora);
});

function getPublicidad(emisora) {
    $('#data_table').DataTable({
        "destroy": true,
        "ajax": {
            "method": "GET",
            "url": "/api/radio/"+ emisora + "/publicidad",
            "dataSrc": "",
            "error": function(xhr, status, error) {
                console.log("readyState: " + xhr.readyState);
                console.log("responseText: "+ xhr.responseText);
                console.log("status: " + xhr.status);
                console.log("text status: " + status);
                console.log("error: " + error);
            },
        },
        "columns": [
            { data: "id"},
            { data: "imagen"},
            { data: "titulo"},
            { data: "cliente"},
            { data: "fecha_inicio"},
            { data: "fecha_fin"},
            { data: "id"}
        ],
        columnDefs: [
            { width: 10, targets: 0},
            { width: 150, targets: 1, render: function(data) {
                return '<img src="' + data + '" width="100%" >';
            }},
            { width: 250, targets: 2},
            { width: 100, targets: 3},
            { width: 150, targets: 4, render: function(data) {
                return `${data.slice(0,10)}`;
            }},
            { width: 150, targets: 5, render: function(data) {
                return `${data.slice(0,10)}`;
            }},
            { width: 150, className: "text-center", targets: 6, render: function(data){
                return `<a href="/publicidad/` + data + `" class="btn btn-primary btn-sm" role="button"><i class="fas fa-eye mx-auto"></i></a>
                        <a href="/publicidad/` + data + `/editar" class="btn btn-success btn-sm" role="button"><i class="fas fa-pen mx-auto"></i></a>
                        <a href="#" onclick="showWarning(` + data + `)" class="btn btn-danger btn-sm" role="button"><i class="fas fa-times mx-auto"></i></a>`
            }},
        ],
    });
}