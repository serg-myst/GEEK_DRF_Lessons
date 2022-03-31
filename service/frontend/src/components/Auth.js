import React, {Component} from 'react'
import {Link} from 'react-router-dom'

class LoginForm extends Component {
    constructor(props) {
        super(props);
        this.state = {login: '',
                      password: ''}
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        });
    }

    handleSubmit(event) {
        this.props.get_token(this.state.login, this.state.password)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <input type='text' name='login' placeholder='login' value={this.state.login} onChange={(event)=>this.handleChange(event)} />
                <input type="password" name="password" placeholder="password" value={this.state.password} onChange={(event)=>this.handleChange(event)} />
                <input type="submit" value="Login" />
                <div>
                    <Link to='/'>На главную</Link>
                </div>
            </form>
        );
    }
}

export default LoginForm;
