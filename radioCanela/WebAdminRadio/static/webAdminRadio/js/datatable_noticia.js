//id del comboboxxxx
$("#emisoraSelect").change(function () {
    var id_emisora = $("#emisoraSelect option:selected").val();
    getNoticia("/api/emisora/"+ id_emisora + "/noticia");
});

// $("#tipoSelect").change(function () {
//     var id_emisora = $("#tipoSelect option:selected").val();
//     getNoticia(id_emisora);
// });

function getNoticia(link) {
    $('#data_table').DataTable({
        "destroy": true,
        "ajax": {
            "method": "GET",
            "url": link,
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
            { data: "radioEmisora"},
            { data: "fecha_subida"},
            { data: "tipo"},
            { data: "id"}
        ],
        columnDefs: [
            { width: 10, targets: 0},
            { width: 200, targets: 1},
            { width: 150, targets: 2},
            { width: 150, targets: 3, render: function(data) {
                return `${data.slice(0,10)}`;
            }},
            { width: 150, targets: 4},
            { width: 150, className: "text-center", targets: 5, render: function(data){
                return `<a href="/noticia/` + data + `" class="btn btn-primary btn-sm" role="button"><i class="fas fa-eye mx-auto"></i></a>
                        <a href="/noticia/` + data + `/editar" class="btn btn-success btn-sm" role="button"><i class="fas fa-pen mx-auto"></i></a>
                        <a href="#" onclick="showWarning(` + data + `)" class="btn btn-danger btn-sm" role="button"><i class="fas fa-times mx-auto"></i></a>`
            }},
        ],
    });
}