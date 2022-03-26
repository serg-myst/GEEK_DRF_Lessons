import React from 'react'
import {Link} from "react-router-dom";

const ProjectItem = ({project}, {index}) => {
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

const ProjectList = ({todo_projects}) => {
    return (
        <div>
            <h2>Список проектов</h2>
            <table>
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
                {todo_projects.map(function (project, i) {
                        return (
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
                            </tr>
                        )
                    }
                )
                }
            </table>
            <div>
                <Link to='/'>На главную</Link>
            </div>
        </div>
    )
}

export default ProjectList