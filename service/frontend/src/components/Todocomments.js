import React from 'react'
import {Link} from "react-router-dom";

const TodoItem = ({todo}) => {
    return (
        <tr>
            <td>
                {todo.project.name}
            </td>
            <td>
                {todo.user.username}
            </td>
            <td>
                {todo.note_text}
            </td>
            <td>
                {todo.create_timestamp}
            </td>
        </tr>
    )
}

const TodoList = ({todo_notes}) => {
    return (
        <div>
            <h2>Сообщения пользователей</h2>
            <table>
                <tr>
                    <th>
                        Project
                    </th>
                    <th>
                        User
                    </th>
                    <th>
                        Note
                    </th>
                    <th>
                        Date
                    </th>
                </tr>
                {todo_notes.map((todo) => <TodoItem todo={todo}/>)}
            </table>
             <div>
                <Link to='/'>На главную</Link>
            </div>
        </div>
    )
}

export default TodoList