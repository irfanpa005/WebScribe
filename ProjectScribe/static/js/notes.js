
document.addEventListener('DOMContentLoaded', function () {

   var sidebarItems = document.querySelectorAll(".snote");

// << --- SideBar Adjusting function --->>
   var resizer = document.querySelector(".resizer")
   var sidebar = document.querySelector(".sidebar");

   function initResizerFn( resizer, sidebar ) {

   // track current mouse position in x var
   var x, w;

   function rs_mousedownHandler( e ) {

      x = e.clientX;
      
      var sbWidth = window.getComputedStyle( sidebar ).width;
      w = parseInt( sbWidth, 10 );

      document.addEventListener("mousemove", rs_mousemoveHandler);
      document.addEventListener("mouseup", rs_mouseupHandler);
   }

   function rs_mousemoveHandler( e ) {
      var dx = e.clientX - x;
      
      var cw = w + dx; // complete width

      if ( cw < 700 && cw > 300 ) { //min and max size of sidebar
         sidebar.style.width = `${ cw }px`;
      }
   }

   function rs_mouseupHandler() {
      // remove event mousemove && mouseup
      document.removeEventListener("mouseup", rs_mouseupHandler);
      document.removeEventListener("mousemove", rs_mousemoveHandler);
   }

   resizer.addEventListener("mousedown", rs_mousedownHandler);
   }

   initResizerFn( resizer, sidebar );

// << --- SideBar Adjusting function End--->>




// << --- First note selected or active--->>

const firstNote = document.querySelector('.snote');

   if (firstNote === null){
      const btnContainer = document.querySelector('.button-container');
      btnContainer.style.display = "none";
   }

   if (firstNote){
      viewNote({target: firstNote});
      firstNote.classList.add('active-li');
   }

// << --- First note selected or active end--->>




// << --- Single Note Display --->>

var shareToggle = document.getElementById('shareBtn')
var shareBtnLabel = document.getElementById('sharelabel')
var noteID = ""


function viewNote (event){
   const objectId = event.target.dataset.objectId;
   const noteDisplayDIv = document.getElementById('dispEl')
   const editLink = document.getElementById('editBtn')
   const confirmDelete = document.getElementById('confirmDelete');
   noteID =objectId;

   editLink.href = `/notes/edit_note/${objectId}/`;
   shareBtn.setAttribute('data-object-id', objectId);
   confirmDelete.setAttribute('data-object-id', objectId);


   const allNoteElements = document.querySelectorAll('.snote');
   allNoteElements.forEach(element => {
       element.classList.remove('active-li');
   });

   event.target.classList.add('active-li');

   fetch(`/notes/note_display/${objectId}/`)
   .then(response => response.json())
   .then(data => {
       // Update the noteDisplayDIv with the fetched data
         noteDisplayDIv.innerHTML = `
         <h4><strong>Title: ${data.title}</strong></h4>
         <p> ${data.content}</p><br><br>
         <p>created at: ${data.created_at}</p>
     `;
     if(data.is_shared === true){
         shareToggle.checked = true
         shareBtnLabel.innerHTML = "note shared"
     } else    {
         shareToggle.checked = false
         shareBtnLabel.textContent = "share note with others"
     }

 });

}

const notes = document.querySelectorAll('.snote');
notes.forEach(note => {
   note.addEventListener('click' , viewNote);
});
// << --- Single Note Display End--->>




// << --- Shared Toggle change--->>

shareToggle.addEventListener("change", function () {
   const noteID = this.dataset.objectId;
   if (shareToggle.checked) {
      shareBtnLabel.textContent = "note shared"
      share_status_update(true)
   } else {
      shareBtnLabel.textContent = "share note with others"
      share_status_update(false)
   }

   function share_status_update(status){

   fetch(`notesharestatus/${noteID}`, {
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

// << --- Shared Toggle Change end--->>





// << --- Side Toggle bar icon--->>

var media600 = window.matchMedia("(max-width: 600px)")
var sbCover = document.querySelector(".sb-cover");

function closeSidebar(){
   sbCover.style.display = "none";
}

document.getElementById("sbToggle").addEventListener("click", function(){

      if (sbCover.style.display === "block"){
         closeSidebar()
      } else {
         sbCover.style.display = "block";
      }
   });

if (media600.matches){

   sidebarItems.forEach(function(item){
      item.addEventListener("click",closeSidebar);
   });


window.addEventListener("click", function (event) {
   if (!event.target.matches("#sbToggle") && !sidebar.contains(event.target) 
   && !event.target.matches(".sb-item")) {
      closeSidebar()
   }
   
});

}

// << --- Side Toggle bar icon end--->>




// << --- note search function--->>

const searcBtn = document.getElementById('search-btn')
const noteDisplayUl = document.getElementById('noteDisplUl')
const noteDisplayDIv = document.getElementById('dispEl')
const serchNotif = document.getElementById('search-result-notf')
const btnContainer = document.querySelector('.button-container');
const noResult = document.getElementById('no-result-found')

document.getElementById('searchform').addEventListener('submit',function(event){
   event.preventDefault();
   noteDisplayUl.innerHTML = " ";
   noResult.textContent = ` `;
   var searchWord = document.getElementById('search-word').value

   if (searchWord){
      serchNotif.style.display = 'block';
      serchNotif.textContent = `showing results for '${searchWord}'`;
   }

 
   fetch(`/notes/user/search/`, {
      method: "POST",
      headers: {
          "Content-type": "application/json",
          "X-CSRFToken": getcookie("csrftoken")
      },
      body: JSON.stringify({
          search_keyword: searchWord
      })
  })
   .then(response => response.json())
   .then(data => {

      if (data.length === 0){
         noteDisplayDIv.textContent=" ";
         btnContainer.style.display = "none";
         noResult.style.display = 'block';
         noResult.textContent = `0 results found for '${searchWord}'`;
      }

      data.forEach(note => {
         const li = document.createElement('li');
         li.textContent = note.title;
         li.classList.add('snote', 'badge');
         li.dataset.objectId = note.pk;
         noteDisplayUl.appendChild(li);
         li.addEventListener('click', viewNote);

         const firstNote = document.querySelector('.snote');

         if (firstNote){
            viewNote({target: firstNote});
            firstNote.classList.add('active-li');
         }

         
         
     });
   })

   .catch(error => console.error('Error fetching filtered notes:', error));
   
   function getcookie(name){
      const value =`; ${document.cookie}`;
      const parts = value.split(`; ${name}=`);
      if (parts.length == 2) return parts.pop().split(';').shift();
      }   
   });

// << --- note search end -->>




// << --- delete modal popup -->>

const deleteButton = document.getElementById('delBtn');
const confirmationPopup = document.getElementById('confirmationPopup');
const confirmDelete = document.getElementById('confirmDelete');
const cancelDelete = document.getElementById('cancelDelete');

deleteButton.addEventListener('click', function (event) {
   event.preventDefault();
   confirmationPopup.style.display = 'block';
});

cancelDelete.addEventListener('click', function () {
   confirmationPopup.style.display = 'none';
});

confirmDelete.addEventListener('click', function(){
   const noteID = this.dataset.objectId;
   var delUrl = `/notes/delete_note/${noteID}/`;
   window.location.href = delUrl;

});

})


