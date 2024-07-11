CREATE TABLE `users` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `nome` varchar(255),
  `email` varchar(255),
  `senha` varchar(255),
  `created at` varchar(255)
);

CREATE TABLE `paciente` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `nome` varchar(255),
  `particular` bool,
  `prontuario` int
);

CREATE TABLE `prontuarios` (
  `id` int AUTO_INCREMENT,
  `nome` varchar(255),
  `queixa` varchar(255),
  `remedios` varchar(255),
  `ultima_data` date
);

CREATE TABLE `atendimento` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `nome` varchar(255),
  `queixa` varchar(255),
  `remedios` varchar(255),
  `atestado` bool,
  `data` date
);

CREATE TABLE `planos` (
  `particular` float,
  `plano` float
);

ALTER TABLE `paciente` ADD FOREIGN KEY (`nome`) REFERENCES `prontuarios` (`nome`);

ALTER TABLE `paciente` ADD FOREIGN KEY (`prontuario`) REFERENCES `prontuarios` (`id`);

ALTER TABLE `atendimento` ADD FOREIGN KEY (`nome`) REFERENCES `paciente` (`nome`);

ALTER TABLE `prontuarios` ADD FOREIGN KEY (`queixa`) REFERENCES `atendimento` (`queixa`);

ALTER TABLE `prontuarios` ADD FOREIGN KEY (`remedios`) REFERENCES `atendimento` (`remedios`);

ALTER TABLE `prontuarios` ADD FOREIGN KEY (`ultima_data`) REFERENCES `atendimento` (`data`);

INSERT INTO `users` (`nome`, `email`, `senha`, `created_at`) VALUES
('User1', 'user1@example.com', 'password1', '2023-01-01'),
('User2', 'user2@example.com', 'password2', '2023-02-01');

INSERT INTO `prontuarios` (`nome`, `queixa`, `remedios`, `ultima_data`) VALUES
('Paciente1', 'Dor de cabeça', 'Paracetamol', '2023-01-10'),
('Paciente2', 'Febre', 'Ibuprofeno', '2023-02-15');

INSERT INTO `paciente` (`nome`, `particular`, `prontuario`) VALUES
('Paciente1', true, 1),
('Paciente2', false, 2);

INSERT INTO `atendimento` (`nome`, `queixa`, `remedios`, `atestado`, `data`) VALUES
('Paciente1', 'Dor de cabeça', 'Paracetamol', false, '2023-01-10'),
('Paciente2', 'Febre', 'Ibuprofeno', true, '2023-02-15');

INSERT INTO `planos` (`particular`, `plano`) VALUES
(200.00, 150.00)