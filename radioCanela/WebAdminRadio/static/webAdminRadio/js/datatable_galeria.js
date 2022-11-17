$("#emisoraSelect").change(function () {
    var id_emisora = $("#emisoraSelect option:selected").val();
    getGaleria(id_emisora);
});

function getGaleria(emisora) {
    $('#data_table').DataTable({
        "destroy": true,
        "ajax": {
            "method": "GET",
            "url": "/api/emisora/"+ emisora +"/galeria",
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
            { data: "url"},
            { data: "titulo"},
            { data: "descripcion"},
            { data: "fecha_creacion"},
            { data: "likes"},
            { data: "id"}
        ],
        columnDefs: [
            { width: 10, className: "text-center", targets: 0},
            { width: 200, className: "text-center", targets: 1, render: function(data) {
                var image = '';
                if (data == null){
                    image = `<img src="/static/webAdminRadio/images/generic_avatar.png" width="100%">`;
                } else {
                    image = '<img src="' + data + '" width="100%" height: 50%">';
                }
                return image;
            }},
            { width: 250, className: "text-center align-items-center", targets: 2},
            { width: 250, className: "text-center", targets: 3},
            { width: 250, className: "text-center", targets: 4, render: function(data){
                return data ? new Date(data).toLocaleDateString() : '----/--/--'
            }},
            { width: 250, className: "text-center", targets: 5},
            { width: 150, className: "text-center", targets: 6, render: function(data){
                return `<a href="/programas/` + data + `" class="btn btn-primary btn-sm" role="button"><i class="fas fa-eye mx-auto"></i></a>
                        <a href="/programas/` + data + `/editar" class="btn btn-success btn-sm" role="button"><i class="fas fa-pen mx-auto"></i></a>
                        <a href="#" onclick="showWarning(` + data + `)" class="btn btn-danger btn-sm" role="button"><i class="fas fa-times mx-auto"></i></a>
                        `
            }},
        ],
    });
}