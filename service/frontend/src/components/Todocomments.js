import React from 'react'
import {Link} from "react-router-dom";
import Table from 'react-bootstrap/Table'

const TodoItem = ({todo, deleteTodo}) => {
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
             <td>
                 <button type='button' onClick={()=>deleteTodo(todo.id)}>Удалить</button>
             </td>
        </tr>
    )
}

const TodoList = ({todo_notes, deleteTodo}) => {
 console.log(deleteTodo)
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
                {todo_notes.map((todo) => <TodoItem todo={todo} deleteTodo={deleteTodo}/>)}
            </Table>
            <div>
                <Link to='/todo/create'>Создать заметку</Link>
            </div>
             <div>
                <Link to='/'>На главную</Link>
            </div>
        </div>
    )
}

export default TodoList