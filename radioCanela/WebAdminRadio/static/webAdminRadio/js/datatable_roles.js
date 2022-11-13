$('#data_table').DataTable({
    destroy: true,
    ajax: {
        method: 'GET',
        url: '/api/roles',
        dataSrc: "",
        error: function(xhr, status, error) {
            console.log("readyState: " + xhr.readyState);
            console.log("responseText: "+ xhr.responseText);
            console.log("status: " + xhr.status);
            console.log("text status: " + status);
            console.log("error: " + error);
        },
    },
    columns: [
        { data: "name" },
        { data: "fecha_creacion" },
        { data: "activo"},
        { data: "id" }
    ],
    columnDefs: [
        { width: 300, targets: 0 },
        { width: 300, targets: 1, render: (data) => new Date(data) },
        { width: 300, targets: 2 },
        { width: 300, targets: 3, render: function(data){
            return `<a href="/roles/${data}/editar" class="btn btn-success btn-sm" role="button"><i class="fas fa-pen mx-auto"></i></a>
                    <a href="#" onclick="showWarning(${data})" class="btn btn-danger btn-sm" role="button"><i class="fas fa-times mx-auto"></i></a>`
        }},
    ],
});