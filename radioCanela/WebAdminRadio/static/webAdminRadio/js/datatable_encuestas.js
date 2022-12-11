$("#emisoraSelect").change(function () {
    var id_emisora = $("#emisoraSelect option:selected").val();
    getSegmentos(id_emisora);
});

function getSegmentos(emisora) {
    $('#data_table').DataTable({
        "destroy": true,
        "ajax": {
            "method": "GET",
            "url": "/api/emisora/"+ emisora +"/encuestas",
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
            { data: "descripcion"},
            { data: "dia_inicio"},
            { data: "dia_fin"},
            { data: "estado"},
            { data: "id"},
        ],
        columnDefs: [
            { width: 10, targets: 0},
            { 
                width: 180, 
                targets: 1, 
                render: function(data){
                    return data ? `<img src="${data}" width="100%"></img>` : '<img src="/static/webAdminRadio/images/redonda.jpg" width="100%">';
                }
            },
            { width: 150, targets: 2},
            { width: 250, targets: 3},
            { width: 150, targets: 4},
            { width: 150, targets: 5},
            { width: 100, targets: 6},
            { 
                width: 200, 
                className: "text-center", 
                targets: 7, 
                render: function(data){
                    return `<a href="/encuestas/${data}" class="btn btn-primary btn-sm" role="button"><i class="fas fa-eye mx-auto"></i></a>
                    <a href="/encuestas/${data}/editar" class="btn btn-success btn-sm" role="button"><i class="fas fa-pen mx-auto"></i></a>
                    <a href="#" onclick="showWarning(${data})" class="btn btn-danger btn-sm" role="button"><i class="fas fa-times mx-auto"></i></a>`
                }
            },
        ],
    });
}