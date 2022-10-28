$("#emisoraSelect").change(function () {
    var id_emisora = $("#emisoraSelect option:selected").val();
    getSegmentos(id_emisora);
});

function getSegmentos(emisora) {
    $('#data_table').DataTable({
        "destroy": true,
        "ajax": {
            "method": "GET",
            "url": "/api/emisora/"+ emisora +"/transmisiones",
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
            { data: "titulo"},
            { data: "plataforma"},
            { data: "plataforma"},
            { data: "id"}
        ],
        columnDefs: [
            { width: 10, targets: 0},
            { width: 200, targets: 1},
            { width: 250, targets: 2, render: function(data) {
                html = ``;
                for (var key in data){
                    html += data[key].plataforma;
                }
                return html;
            }},
            { width: 250, targets: 3, render: function(data) {
                html = ``;
                for (var key in data){
                    html += data[key].url;
                }
                return html;
            }},
            { width: 150, className: "text-center", targets: 4, render: function(data){
                return `<a href="/transmision/` + data + `/editar" class="btn btn-success btn-sm" role="button"><i class="fas fa-pen mx-auto"></i></a>
                        <a href="#" onclick="showWarning(` + data + `)" class="btn btn-danger btn-sm" role="button"><i class="fas fa-times mx-auto"></i></a>
                        `
            }},
        ],
    });
}