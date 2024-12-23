import React, { useState } from "react";
import { useNavigate } from "react-router-dom"; // Import useNavigate for redirection
import axios from "axios";
import "./Register.css"; // Import the CSS file

export default function Register() {
	const navigate = useNavigate(); // Hook to navigate programmatically

	const [formData, setFormData] = useState({
		username: "",
		email: "",
		password1: "",
		password2: "",
	});

	const handleChange = (e) => {
		setFormData({
			...formData,
			[e.target.name]: e.target.value,
		});
	};

	const [isLoading, setIsLoading] = useState(false);
	const [successMessage, setSuccessMessage] = useState(null);
	const [error, setError] = useState(null);

	const handleSubmit = async (e) => {
		e.preventDefault();
		if (isLoading) {
			return;
		}

		setIsLoading(true);

		try {
			const response = await axios.post("http://127.0.0.1:8000/api/register/", formData);
			console.log("Success!", response.data);
			setSuccessMessage("Registration Successful!");

			window.location.href = "/";
		} catch (error) {
			console.log("Error during registration!", error.response?.data);
			if (error.response && error.response.data) {
				Object.keys(error.response.data).forEach((field) => {
					const errorMessages = error.response.data[field];
					if (errorMessages && errorMessages.length > 0) {
						setError(errorMessages[0]);
					}
				});
			}
		} finally {
			setIsLoading(false);
		}
	};

	const handleLoginRedirect = () => {
		navigate("/login"); // Redirect to the login page
	};

	return (
		<div className="register-container">
			{error && <p className="error-message">{error}</p>}
			{successMessage && <p className="success-message">{successMessage}</p>}
			<div className="register-card">
				<h2 className="register-title">Register</h2>
				<form className="register-form">
					<label>Username</label>
					<input
						type="text"
						name="username"
						value={formData.username}
						onChange={handleChange}
						placeholder="Enter your username"
					/>
					<label>Email</label>
					<input
						type="email"
						name="email"
						value={formData.email}
						onChange={handleChange}
						placeholder="Enter your email"
					/>
					<label>Password</label>
					<input
						type="password"
						name="password1"
						value={formData.password1}
						onChange={handleChange}
						placeholder="Enter your password"
					/>
					<label>Confirm Password</label>
					<input
						type="password"
						name="password2"
						value={formData.password2}
						onChange={handleChange}
						placeholder="Re-enter your password"
					/>
					<button
						type="submit"
						disabled={isLoading}
						onClick={handleSubmit}
						className="register-button"
					>
						{isLoading ? "Registering..." : "Register"}
					</button>
				</form>
				{/* Add Login Button */}
				<div className="login-redirect-container">
					<p >Already have an account?</p>
					<button onClick={handleLoginRedirect} className="login-button">
						Login
					</button>
				</div>
			</div>
		</div>
	);
}
