document.addEventListener('DOMContentLoaded',function(){

    const addButton = document.getElementById("addBtn")
    const popcancButton = document.getElementById("popcanceltuto")

    const editButton = document.querySelectorAll(".editBtn")
    const delButton = document.querySelectorAll(".delBtn")

    const addTutWindow = document.getElementById("addTutorialWindow")
    const tutoForm = document.getElementById("tutorialform")
    const tutoFormTitle = document.querySelector(".modal-title")
    const addTutoButton = document.getElementById("submit-id-submit")
    const tutoFormdefaultAction = tutoForm.getAttribute('action');

    const confirmationPopup = document.getElementById('confirmationPopup');
    const confirmDelete = document.getElementById('confirmDelete');
    const cancelDelete = document.getElementById('cancelDelete');

    var shareToggle = document.querySelectorAll('.form-check-input')

    addButton.addEventListener("click", function(event){
        event.preventDefault();
        addTutWindow.style.display = "block";
        tutoFormTitle.textContent = `Add new Tutorial`;
        addTutoButton.setAttribute("value", "Add Tutorial");

        document.getElementById('id_title').value = "";
        document.getElementById('id_short_descr').value = "";
        document.getElementById('id_link').value = "";
        document.getElementById('id_is_shared').checked = false;
       
        tutoForm.setAttribute("action", tutoFormdefaultAction);

    });

    popcancButton.addEventListener("click", function(event){
        event.preventDefault();
        addTutWindow.style.display = "none";

    });


// << --- Edit tutorial popup button  -->>

editButton.forEach(btn =>{
    btn.addEventListener("click",function(event){
        event.preventDefault();
        addTutWindow.style.display = "block";
        const tutoId = event.target.dataset.objectId;
        const url = `/notes/edit_tutorial/${tutoId}`; 
        tutoForm.setAttribute("action", url);
        tutoFormTitle.textContent = `Edit Tutorial`;
        addTutoButton.setAttribute("value", "Update Tutorial")

        fetch(`/notes/edit_tutorial/${tutoId}`, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
            },
        })
         .then(response => response.json())
         .then(data => {
                // Populate the form fields with the received data
                document.getElementById('id_title').value = data.title;
                document.getElementById('id_short_descr').value = data.short_descr;
                document.getElementById('id_link').value = data.link;
                document.getElementById('id_is_shared').checked = data.is_shared;
         })
         .catch(error => {
            console.error('Error:', error);
        });
    });
});


delButton.forEach(btn => {
    btn.addEventListener("click", function(event){
        event.preventDefault();
        const tutoId = event.target.dataset.objectId;
        confirmationPopup.style.display = "block";
        confirmDelete.setAttribute("data-object-id",tutoId)
    });
});


confirmDelete.addEventListener("click", function(event){
    event.preventDefault();
    var tutoId = this.dataset.objectId;
    var delUrl = `/notes/delete_tutorial/${tutoId}`;
    window.location.href = delUrl;
  
});


cancelDelete.addEventListener("click", (event)=>{
    event.preventDefault();
    confirmationPopup.style.display ="none";
});



shareToggle.forEach(function (button)  {
    button.addEventListener("change", function (event) {
        var tutoId = button.getAttribute("data-object-id");
        const shareBtnLabel = document.querySelector(`#sharelabel${tutoId}`);
        if (button.checked) {
           shareBtnLabel.textContent = "tutorial shared"
           share_status_update(true)
        } else {
           shareBtnLabel.textContent = "share tutorial with others"
           share_status_update(false)
        }
     
        function share_status_update(status){
     
        fetch(`/notes/tutorial_sharestatus/${tutoId}`, {
           method: "POST",
           headers: {
               "Content-type": "application/json",
               "X-CSRFToken": getcookie("csrftoken")
           },
           body: JSON.stringify({
               isShared: status,
           })
        })
        .then(function (response) {
           if (response.status === 200) {
                 console.log("Note updated successfully");
           } else {
                 console.error("Error updating note");
           }
        })
        .catch(function(error){
        console.error("Fetch error:", error);
        });
     
     
     
        function getcookie(name){
           const value =`; ${document.cookie}`;
           const parts = value.split(`; ${name}=`);
           if (parts.length == 2) return parts.pop().split(';').shift();
           }   
     
        }
     
     });

});


});