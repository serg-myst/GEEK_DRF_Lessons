import React from 'react'
import {Link} from "react-router-dom";

const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                {user.username}
            </td>
            <td>
                {user.email}
            </td>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
            </td>
        </tr>
    )
}

const UserList = ({todo_users}) => {
    return (
        <div>
            <h2>Список пользователей</h2>
            <table>
                <tr>
                    <th>
                        Name
                    </th>
                    <th>
                        email
                    </th>
                    <th>
                        First name
                    </th>
                    <th>
                        Last name
                    </th>
                </tr>
                {todo_users.map((user) => <UserItem user={user}/>)}
            </table>
             <div>
                <Link to='/'>На главную</Link>
            </div>
        </div>
    )
}


export default UserList