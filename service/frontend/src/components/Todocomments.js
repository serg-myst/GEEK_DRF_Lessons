import React from 'react'
import {Link} from "react-router-dom";
import Table from 'react-bootstrap/Table'

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
            <Table responsive>
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
            </Table>
             <div>
                <Link to='/'>На главную</Link>
            </div>
        </div>
    )
}

export default TodoList