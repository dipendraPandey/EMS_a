"use strict";

let deleteEmployee11 = ((id, csrftoken) => {
    swal({
        title: 'Are you sure?',
        text: 'Once deleted, you will not be able to recover Employee date!',
        icon: 'warning',
        buttons: true,
        dangerMode: true,
    }).then((willDelete) => {
        if (willDelete) {
            $.ajax({
                type: 'POST',
                url: `http://localhost:8002/employee/delete/${id}/`,
                data: {
                    csrfmiddlewaretoken: csrftoken
                },

                success: (response) => {
                    console.log(response);
                    swal({
                        title: 'Poof! Employee has been deleted!',
                        icon: 'success',
                    }).then(value =>{
                        if(value){
                            window.location = '/employee/list'
                        }
                    })

                },
                error: function () {
                    swal({
                        title: 'Employee delete Error ',
                        icon: 'error'
                    })
                }
            })


        }
    })
});

$("#swal-8").click(function () {
  swal('This modal will disappear soon!', {
    buttons: false,
    timer: 3000,
  });
});
