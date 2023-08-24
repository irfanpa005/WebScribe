
document.addEventListener('DOMContentLoaded',function(){

const addtaskButton = document.getElementById("addBtn")
const popaddButton = document.getElementById("popaddtaskbtn")
const popcancButton = document.getElementById("popcanceltask")


const editButton = document.querySelectorAll(".editBtn")
const delButton = document.getElementById("delBtn")
const doneButton = document.getElementById("doneBtn")

const addTaskWindow = document.getElementById("addTaskWindow")
const taskForm = document.getElementById("taskform")
const taskFormTitle = document.querySelector(".modal-title")
const addNoteButton = document.getElementById("submit-id-submit")


// << --- Add task button popup -->>
addtaskButton.addEventListener("click", function(event){
    event.preventDefault();
    addTaskWindow.style.display = "block";
    // taskForm.setAttribute("action", "{% url 'toDo:addTask' request.user %}");
    taskFormTitle.textContent = `Add new Task`
    addNoteButton.setAttribute("value", "Add Note")

});


// << --- Cancel popup button  -->>
popcancButton.addEventListener("click", function(){
    addTaskWindow.style.display = "none";

});


// << --- Edit task popup button  -->>

editButton.forEach(btn =>{
    btn.addEventListener("click",function(event){
        event.preventDefault;
        const taskId = this.getAttribute('data-task-id');
        addTaskWindow.style.display = "block";
        taskForm.setAttribute("action", "{% url 'toDo:editTask' request.user %}")
        taskFormTitle.textContent = `Edit Task`;
        addNoteButton.setAttribute("value", "Update Note")

        console.log(taskId)

        fetch(`edit_task/${taskId}`, {
            method: "POST",
            headers: {
                "Content-type": "application/json",
                "X-CSRFToken": getcookie("csrftoken")
            },
            body: JSON.stringify({
                // empty body
            })
         })
         .then(response => response.json())
         .then(data => {
            console.log(data)
         });







        //  .then(function (response) {
        //     if (response.status === 200) {
        //           console.log("Edit for passed successfully");
        //     } else {
        //           console.error("Error passing form");
        //     }
        //  })
        //  .catch(function(error){
        //  console.error("Fetch error:", error);
        //  });
      
    
    });

});





function getcookie(name){
    const value =`; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length == 2) return parts.pop().split(';').shift();
    }   


});