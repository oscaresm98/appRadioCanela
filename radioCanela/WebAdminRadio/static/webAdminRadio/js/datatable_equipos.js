$('#data_table').DataTable({
    "destroy": true,
    "ajax": 
        {
        "method": "GET",
        "url": "/api/equipos",
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
        { data: "equipo"},
        { data: "ciudad"},
        { data: "estado"},
        { data: "id"}
    ],
    columnDefs: [
        { width: 10, className: "text-center", targets: 0},
        { width: 200, targets: 1, render: function(data) {
            var image = '';
            if (data == null){
                image = `<img src="/static/webAdminRadio/images/generic_avatar.png" width="100%">`;
            } else {
                image = '<img src="' + data + '" width="100%" height: 50%">';
            }
            return image;
        }},
        { width: 250, targets: 2},
        { width: 200, targets: 3},
        { width: 100, targets: 4},
        { width: 200, className: "text-center", targets: 5, render: function(data){
            return `<a href="/equipos/` + data + `" class="btn btn-primary btn-sm" role="button"><i class="fas fa-eye mx-auto"></i></a>
                    <a href="/equipos/` + data + `/editar" class="btn btn-success btn-sm" role="button"><i class="fas fa-pen mx-auto"></i></a>
                    <a href="#" onclick="showWarning(` + data + `)" class="btn btn-danger btn-sm" role="button"><i class="fas fa-times mx-auto"></i></a>
                    `
        }},
    ],
});