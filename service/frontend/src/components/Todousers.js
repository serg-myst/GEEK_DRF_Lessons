import React from 'react'

const UserItem = ({user}) => {
    return (
        <tr>
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
        <table>
            <th>
                email
            </th>
            <th>
                First name
            </th>
            <th>
                Last name
            </th>
            {todo_users.map((user) => <UserItem user={user} />)}
        </table>
    )
}


export default UserList