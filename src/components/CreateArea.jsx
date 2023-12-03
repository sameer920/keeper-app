import React, { useState } from "react";
import {Fab, Zoom} from '@mui/material';
import AddIcon from '@mui/icons-material/Add';

function CreateArea(props) {
    const [note, addNote] = useState({ title: "", content: "" });

    function handleChange(event) {
        const { name, value } = event.target;
        addNote((prevValue) => {
            return {
                ...prevValue,
                [name]: value
            };
        });
    }

    function addNewNote(event) {
        props.addNote(note);
        event.preventDefault();
        addNote({ title: "", content: "" });
    }

    return (
        <div>
            <form className="create-note" onSubmit={addNewNote}>
                {props.clicked && <input name="title" onChange={handleChange} onClick={(event)=>event.stopPropagation()} placeholder="Title" value={note.title} autoFocus/>}
                <textarea
                    name="content"
                    className="noteTextArea"
                    onClick={(event) => {props.handleClick(true);
                                        event.stopPropagation()}}
                    onChange={handleChange}
                    placeholder="Take a note..."
                    rows={props.clicked ? "3" : "1"}
                    value={note.content}
                />

                <Zoom in={props.clicked} timeout={300}>
                    <Fab type="submit" aria-label="add">
                        <AddIcon />
                    </Fab>
                </Zoom>
            </form>
        </div>
    );
}

export default CreateArea;
