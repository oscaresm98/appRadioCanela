$('#data_table').DataTable({
    "destroy": true,
    "ajax": 
        {
        "method": "GET",
        "url": "/api/locutores",
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
        { data: "nombre"},
        { data: "descripcion"},
        { data: "fecha_nacimiento"},
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
        { width: 100, targets: 4, render: function(data){
            return data ? new Date(data).toLocaleDateString() : '----/--/--'
        }},
        { width: 100, targets: 5, render: function(data){
            var activo = ''
            if (data){
                activo = 'Activo'
            } else {
                activo = 'Inactivo'
            }
            return activo
        }},
        { width: 200, className: "text-center", targets: 6, render: function(data){
            return `<a href="/locutores/` + data + `" class="btn btn-primary btn-sm" role="button"><i class="fas fa-eye mx-auto"></i></a>
                    <a href="/locutores/` + data + `/editar" class="btn btn-success btn-sm" role="button"><i class="fas fa-pen mx-auto"></i></a>
                    <a href="#" onclick="showWarning(` + data + `)" class="btn btn-danger btn-sm" role="button"><i class="fas fa-times mx-auto"></i></a>
                    `
        }},
    ],
});