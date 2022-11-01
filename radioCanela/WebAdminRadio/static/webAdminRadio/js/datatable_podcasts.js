$("#emisoraSelect").change(function () {
    var id_emisora = $("#emisoraSelect option:selected").val();
    getSegmentos(id_emisora);
});

function getSegmentos(emisora) {
    $('#data_table').DataTable({
        "destroy": true,
        "ajax": {
            "method": "GET",
            "url": "/api/emisora/"+ emisora +"/podcasts",
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
            { data: "nombre"},
            { data: "descripcion"},
            { data: "fecha"},
            { data: "audio"},
            { data: "activo"},
            { data: "id"}
        ],
        columnDefs: [
            { width: 10, targets: 0},
            { width: 200, targets: 1},
            { width: 250, targets: 2},
            { width: 150, targets: 4, render: function(data) {
                return `${data.slice(0,10)}`;
            }},
            { width: 250, targets: 4},
            { width: 200, targets: 5},
            { width: 250, className: "text-center", targets: 7, render: function(data){
                return `<a href="/podcasts/` + data + `" class="btn btn-primary btn-sm" role="button"><i class="fas fa-eye mx-auto"></i></a>
                        <a href="/podcasts/` + data + `/editar" class="btn btn-success btn-sm" role="button"><i class="fas fa-pen mx-auto"></i></a>
                        <a href="#" onclick="showWarning(` + data + `)" class="btn btn-danger btn-sm" role="button"><i class="fas fa-times mx-auto"></i></a>`
            }},
        ],
    });
}