import React from "react";
import {Link, useParams} from 'react-router-dom'


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
            <table>
                <tr>
                    <th>Name</th>
                    <th>Description</th>
                    <th>Href</th>
                </tr>
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
            </table>
            <h3>Участники проекта</h3>
            <table>
                <tr>
                    <th>N</th>
                    <th>Name</th>
                    <th>Email</th>
                </tr>
                    {filtered_project[0].users.map(function (user, i) {
                            return (
                                <tr>
                                    <th>
                                        {i+1}
                                    </th>
                                    <th>
                                        {user.username}
                                    </th>
                                    <th>
                                        {user.email}
                                    </th>
                                </tr>
                            )
                        }
                    )
                    }
            </table>
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