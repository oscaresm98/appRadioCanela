$('#data_table').DataTable({
    "destroy": true,
    "ajax": 
        {
        "method": "GET",
        "url": "/api/usuarios",
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
        { data: "foto"},
        { data: "first_name"},
        { data: "fechaNacimiento"},
        { data: "email"},
        { data: "nombreRol"},
        { data: "date_joined"},
        { data: "activo"},
        { data: "id"}
    ],
    columnDefs: [
        { width: 10, className: "text-center", targets: 0},
        { width: 200, targets: 1, render: function(data) {
            var image = '';
            if (data == null){
                image = `<img src="/static/webAdminRadio/images/generic_avatar.png" width="100%">`;
            } else {
                image = '<img src="' + data + '" width="100%">';
            }
            return image;
        }},
        { width: 200, targets: 2},
        { width: 40, targets: 3},
        { width: 200, targets: 4},
        { width: 50, targets: 5},
        { width: 40, targets: 6, render: function(data) {
            return `${data.slice(0,10)}`;
        }},
        { width: 100, targets: 7},
        { width: 100, className: "text-center", targets: 8, render: function(data){
            return `<a href="/usuarios/editar` + data +`" class="btn btn-success btn-sm" role="button"><i class="fas fa-pen mx-auto"></i></a>
                    <a href="#" onclick="showWarning(` + data + `)" class="btn btn-danger btn-sm" role="button"><i class="fas fa-times mx-auto"></i></a>
                    `
        }},
    ],
});