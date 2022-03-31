import React from "react";
import {Link, useParams} from 'react-router-dom'

import Table from 'react-bootstrap/Table'


const ProjectDetails = ({todo_projects}) => {
    let params = useParams()
    let id = params.id
    console.log(id)
    console.log(todo_projects)
    let filtered_project = todo_projects.filter((project) => project.id == id)
    console.log(filtered_project)
    return (
        <div>
            <h2>Подробно о проекте "{filtered_project[0].name}"</h2>
            <Table responsive>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Description</th>
                        <th>Href</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>
                            {filtered_project[0].name}
                        </td>
                        <td>
                            {filtered_project[0].description}
                        </td>
                        <td>
                            {filtered_project[0].href}
                        </td>
                    </tr>
                </tbody>
            </Table>
            <h3>Участники проекта</h3>
            <Table responsive>
                <thead>
                    <tr>
                        <th>N</th>
                        <th>Name</th>
                        <th>Email</th>
                    </tr>
                </thead>
                    {filtered_project[0].users.map(function (user, i) {
                            return (
                                <tbody>
                                    <tr>
                                        <td>
                                            {i+1}
                                        </td>
                                        <td>
                                            {user.username}
                                        </td>
                                        <td>
                                            {user.email}
                                        </td>
                                    </tr>
                                </tbody>
                            )
                        }
                    )
                    }
            </Table>
            <div>
                <Link to='/'>На главную</Link>
            </div>
            <div>
                <Link to='/projects'>К списку проектов</Link>
            </div>
        </div>
    )
}

export default ProjectDetails