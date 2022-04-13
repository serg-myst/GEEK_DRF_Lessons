import React from 'react'
import {Link} from "react-router-dom";

import Table from 'react-bootstrap/Table'

/* Не используется. Весь вывод в ProjectList
const ProjectItem = (project, index) => {
    return (
        <tr key={index}>
            <td>
                {index}
            </td>
            <td>
                {project.name}
            </td>
            <td>
                {project.href}
            </td>
            <td>
                {project.description}
            </td>
        </tr>
    )
}
 */

const ProjectList = ({todo_projects, deleteProject}) => {
    return (
        <div>
            <h2>Список проектов</h2>
            <Table striped responsive>
                <thead key={'thead'}>
                    <tr>
                        <th>
                            N
                        </th>
                        <th>
                            name
                        </th>
                        <th>
                            href
                        </th>
                        <th>
                            description
                        </th>
                    </tr>
                </thead>
                {todo_projects.map(function (project, i) {
                        return (
                            <tbody key={i}>
                                <tr key={i}>
                                    <td>
                                        {i + 1}
                                    </td>
                                    <td>
                                        <Link to={`project/${project.id}`}>{project.name}</Link>
                                    </td>
                                    <td>
                                        {project.href}
                                    </td>
                                    <td>
                                        {project.description}
                                    </td>
                                    <td>{project.id}</td>

                                    <td>
                                        <button type='button' onClick={()=>deleteProject(project.id)}>Удалить</button>
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
        </div>
    )
}

export default ProjectList