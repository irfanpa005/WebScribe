
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

      if ( cw < 700 && cw > 250 ) {
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

   if (firstNote){
      viewNote({target: firstNote});
      firstNote.classList.add('active-li');
   }

// << --- First note selected or active end--->>


// << --- Single Note Display --->>

function viewNote (event){
   const objectId = event.target.dataset.objectId;
   const noteDisplayDIv = document.getElementById('dispEl');

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
         <h3><strong>Title: ${data.title}</strong></h3>
         <p> ${data.content}</p>
         <p>created at: ${data.created_at}</p>
     `;
 });

}

const notes = document.querySelectorAll('.snote');
notes.forEach(note => {
   note.addEventListener('click' , viewNote);
});
// << --- Single Note Display End--->>


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


document.getElementById('searchform').addEventListener('submit',function(event){
   event.preventDefault();
   noteDisplayUl.innerHTML = " "
   var searchWord = document.getElementById('search-word').value
 
   fetch(`user/search/`, {
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






})


