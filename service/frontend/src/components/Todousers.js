import React from 'react'
import {Link} from "react-router-dom";

import Table from 'react-bootstrap/Table'

const UserItem = ({user, index}) => {
    return (
        <tbody key={'tbody'}>
            <tr key={index}>
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
        </tbody>
    )
}

const UserList = ({todo_users}) => {
    return (
        <div>
            <h2>Список пользователей</h2>
            <Table striped bordered hover size="sm">
                <thead key={'thead'}>
                    <tr key={'tr'}>
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
                </thead>
                {todo_users.map((user, i) => <UserItem user={user} index={i}/>)}
            </Table>
             <div>
                <Link to='/'>На главную</Link>
            </div>
        </div>
    )
}


export default UserList