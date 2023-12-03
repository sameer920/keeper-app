import React, { useEffect, useState } from "react";
import CreateArea from "./CreateArea";

import Footer from "./footer";
import Header from "./header";
import Note from "./Note";


function App() {
    const [notes, updateNotes] = useState([]);
    const [clicked, toggleClick] = useState(false);

    function addNote(note) {
        updateNotes((notesPresent) => {
            let newNote = {
                ...note,
                key: notesPresent.length
            };
            return [ ...notesPresent, newNote];
        })
    }

    function deleteNote(id){
        updateNotes((notesPresent) => {
            return notesPresent.filter((note)=>{
                return note.key !== id;
            });
        });
    }

    function handleClick(value){
        toggleClick(value);
    }

    //Collapse the input area when the user clicks somewhere in the body other than the input area.
    useEffect(()=>{
        function callOnClick(){
            toggleClick(false);
        }
        document.addEventListener("click", callOnClick);
    });

    return <div >
        <Header />
        <CreateArea addNote={addNote} handleClick={handleClick} clicked={clicked} />
        {notes.map(note => <Note key={note.key} deleteNote={deleteNote} id={note.key} title={note.title} content={note.content} />)}
        <Footer />
    </div>
}

export default App;