
document.addEventListener('DOMContentLoaded',function(){

const addtaskButton = document.getElementById("addBtn")
const popaddButton = document.getElementById("popaddtaskbtn")
const popcancButton = document.getElementById("popcanceltask")


const editButton = document.querySelectorAll(".editBtn")
const delButton = document.querySelectorAll(".delBtn")
const doneButton = document.getElementById("doneBtn")

const addTaskWindow = document.getElementById("addTaskWindow")
const taskForm = document.getElementById("taskform")
const taskFormTitle = document.querySelector(".modal-title")
const taskFormdefaultAction = taskForm.getAttribute('action');
const addNoteButton = document.getElementById("submit-id-submit")

const confirmationPopup = document.getElementById('confirmationPopup');
const confirmDelete = document.getElementById('confirmDelete');
const cancelDelete = document.getElementById('cancelDelete');


// << --- Add task button popup -->>
addtaskButton.addEventListener("click", function(event){
    event.preventDefault();
    addTaskWindow.style.display = "block";
    taskFormTitle.textContent = `Add new Task`
    addNoteButton.setAttribute("value", "Add Task")

    document.getElementById('id_title').value = "";
    document.getElementById('id_details').value = "";
    document.getElementById('id_priority').value = "";
    document.getElementById('id_due_date').value = "";

    taskForm.setAttribute("action", taskFormdefaultAction);

});


// << --- Cancel popup button  -->>
popcancButton.addEventListener("click", function(){
    addTaskWindow.style.display = "none";

});


// << --- Edit task popup button  -->>

editButton.forEach(btn =>{
    btn.addEventListener("click",function(event){
        event.preventDefault();
        const taskId = event.target.dataset.objectId;
        const url = `/todo/edit_task/${taskId}`; 
        addTaskWindow.style.display = "block";
        taskForm.setAttribute("action", url);
        taskFormTitle.textContent = `Edit Task`;
        addNoteButton.setAttribute("value", "Update Task")


        fetch(`/todo/edit_task/${taskId}`, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
            },
        })
         .then(response => response.json())
         .then(data => {
                // Populate the form fields with the received data
                document.getElementById('id_title').value = data.title;
                document.getElementById('id_details').value = data.details;
                // Set the checked state for a checkbox (assuming 'is_Active' is a BooleanField)
                document.getElementById('id_is_Active').checked = data.is_active;
                document.getElementById('id_priority').value = data.priority;
                document.getElementById('id_due_date').value = data.due_date;
         })
         .catch(error => {
            console.error('Error:', error);
        });

    });

});


delButton.forEach(btn => {
    btn.addEventListener("click", function(event){
        event.preventDefault();
        const taskId = event.target.dataset.objectId;
        confirmationPopup.style.display = 'block';
        confirmDelete.setAttribute("data-object-id",taskId)
    });
});

confirmDelete.addEventListener("click", function(event){
    var taskId = this.dataset.objectId;
    console.log(taskId)
    var delUrl = `/todo/delete_task/${taskId}`;
    window.location.href = delUrl;

   
});

cancelDelete.addEventListener("click", ()=>{
    confirmationPopup.style.display ="none";
});


   function getcookie(name){
      const value =`; ${document.cookie}`;
      const parts = value.split(`; ${name}=`);
      if (parts.length == 2) return parts.pop().split(';').shift();
      }   






});