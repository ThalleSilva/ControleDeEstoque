-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 11/10/2024 às 12:47
-- Versão do servidor: 8.3.0
-- Versão do PHP: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `emc`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `auditoria`
--

DROP TABLE IF EXISTS `auditoria`;
CREATE TABLE IF NOT EXISTS `auditoria` (
  `id_auditoria` int NOT NULL AUTO_INCREMENT,
  `id_produto` int NOT NULL,
  `produto` varchar(255) NOT NULL,
  `tipo` varchar(20) DEFAULT NULL,
  `descricao` varchar(100) DEFAULT NULL,
  `data_remove` date DEFAULT NULL,
  PRIMARY KEY (`id_auditoria`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `auditoria`
--

INSERT INTO `auditoria` (`id_auditoria`, `id_produto`, `produto`, `tipo`, `descricao`, `data_remove`) VALUES
(3, 2312431, 'teste', 'teste', 'O produtoteste foi exluído na data 2024-10-08 09:58:25', '2024-10-08');

-- --------------------------------------------------------

--
-- Estrutura para tabela `controle`
--

DROP TABLE IF EXISTS `controle`;
CREATE TABLE IF NOT EXISTS `controle` (
  `id` int NOT NULL AUTO_INCREMENT,
  `emc_num` int NOT NULL,
  `descricao` varchar(100) DEFAULT NULL,
  `tipo` varchar(20) DEFAULT NULL,
  `setor` varchar(50) DEFAULT NULL,
  `data_alocacao` date DEFAULT NULL,
  `valor` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=171 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `controle`
--

INSERT INTO `controle` (`id`, `emc_num`, `descricao`, `tipo`, `setor`, `data_alocacao`, `valor`) VALUES
(1, 57115, 'MONITOR DELL P1913SB', 'Monitor', 'Planejamento', '2024-06-16', 10),
(2, 58169, 'COMPUTADOR DELL OPTIPLEX 9020SFF', 'Computador', 'TI', '2024-06-16', 90),
(3, 53638, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(4, 52198, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(5, 48591, 'MONITOR DELL P1913SB', 'Monitor', 'Planejamento', '2024-06-16', 10),
(6, 47908, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(7, 47833, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(8, 47107, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(9, 47023, 'MONITOR DELL P1913SB', 'Monitor', 'Monitoria', '2024-06-16', 10),
(10, 46937, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(11, 46933, 'MONITOR DELL P1913SB', 'Monitor', 'Monitoria', '2024-06-16', 10),
(12, 46918, 'MONITOR DELL P1913SB', 'Monitor', 'Monitoria', '2024-06-16', 10),
(13, 72196, 'COMPUTADOR DELL OPTIPLEX 9020SFF', 'Computador', 'Planejamento', '2024-06-16', 90),
(14, 71518, 'COMPUTADOR DELL OPTIPLEX 9020SFF', 'Computador', 'BMG', '2024-06-16', 90),
(15, 62739, 'COMPUTADOR DELL OPTIPLEX 9020SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(16, 60372, 'COMPUTADOR DELL OPTIPLEX 9020SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(17, 58754, 'COMPUTADOR DELL OPTIPLEX 9020SFF', 'Computador', 'BNB', '2024-06-16', 90),
(18, 58660, 'COMPUTADOR DELL OPTIPLEX 9020SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(19, 72201, 'COMPUTADOR DELL OPTIPLEX 9020SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(20, 47018, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(21, 47024, 'MONITOR DELL P1913SB', 'Monitor', 'BMG', '2024-06-16', 10),
(22, 47192, 'MONITOR DELL P1913SB', 'Monitor', 'Monitoria', '2024-06-16', 10),
(23, 47201, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(24, 47221, 'MONITOR DELL P1913SB', 'Monitor', 'Monitoria', '2024-06-16', 10),
(25, 138898, 'MONITOR DELL P2422H', 'Monitor', 'TI', '2024-06-16', 40),
(26, 47238, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(27, 47999, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(28, 48005, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(29, 49168, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(30, 57421, 'COMPUTADOR DELL OPTIPLEX 9020SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(31, 57433, 'COMPUTADOR DELL OPTIPLEX 9020SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(32, 58265, 'COMPUTADOR DELL OPTIPLEX 9020SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(33, 47299, 'MONITOR DELL P1913SB', 'Monitor', 'BI', '2024-06-16', 10),
(34, 58086, 'COMPUTADOR DELL OPTIPLEX 9020SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(35, 81701, 'COMPUTADOR DELL OPTIPLEX 5050SFF', 'Computador', 'Ole - Treinamento', '2024-06-16', 90),
(36, 81702, 'COMPUTADOR DELL OPTIPLEX 5050SFF', 'Computador', 'Execução', '2024-06-16', 90),
(37, 78817, 'COMPUTADOR DELL OPTIPLEX 5050SFF', 'Computador', 'Planejamento', '2024-06-16', 90),
(38, 81643, 'COMPUTADOR DELL OPTIPLEX 5050SFF', 'Computador', 'BNB', '2024-06-16', 90),
(39, 81904, 'COMPUTADOR DELL OPTIPLEX 5050SFF', 'Computador', 'Planejamento', '2024-06-16', 90),
(40, 81905, 'COMPUTADOR DELL OPTIPLEX 5050SFF', 'Computador', 'Ativos', '2024-06-16', 90),
(41, 82005, 'COMPUTADOR DELL OPTIPLEX 5050SFF', 'Computador', 'BMG', '2024-06-16', 90),
(42, 83168, 'COMPUTADOR DELL OPTIPLEX 5050SFF', 'Computador', 'TI', '2024-06-16', 90),
(43, 97609, 'MONITOR DELL P2319H', 'Monitor', 'Ole - Treinamento', '2024-06-16', 20),
(44, 83171, 'COMPUTADOR DELL OPTIPLEX 5050SFF', 'Computador', 'BMG', '2024-06-16', 90),
(45, 78878, 'MONITOR DELL P2217H', 'Monitor', 'Estoque - TI', '2024-06-16', 20),
(46, 81733, 'MONITOR DELL P2217H', 'Monitor', 'Contabilidade', '2024-06-16', 20),
(47, 81968, 'MONITOR DELL P2217H', 'Monitor', 'TI', '2024-06-16', 20),
(48, 82025, 'MONITOR DELL P2217H', 'Monitor', 'Ole - Treinamento', '2024-06-16', 20),
(49, 84306, 'MONITOR DELL P2217H', 'Monitor', 'Ole - Treinamento', '2024-06-16', 20),
(50, 85661, 'MONITOR DELL P2217H', 'Monitor', 'Ole - Treinamento', '2024-06-16', 20),
(51, 83291, 'COMPUTADOR DELL OPTIPLEX 5050SFF', 'Computador', 'Ole - Treinamento', '2024-06-16', 90),
(52, 71396, 'COMPUTADOR DELL OPTIPLEX 9020SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(53, 75753, 'MONITOR DELL P2317H', 'Monitor', 'Ole - Treinamento', '2024-06-16', 20),
(54, 75201, 'MONITOR DELL P2317H', 'Monitor', 'Ole - Treinamento', '2024-06-16', 20),
(55, 83165, 'COMPUTADOR DELL OPTIPLEX 5050SFF', 'Computador', 'Ole - Treinamento', '2024-06-16', 90),
(56, 83184, 'COMPUTADOR DELL OPTIPLEX 5050SFF', 'Computador', 'Ole - Treinamento', '2024-06-16', 90),
(57, 83186, 'COMPUTADOR DELL OPTIPLEX 5050SFF', 'Computador', 'Ole - Treinamento', '2024-06-16', 90),
(58, 83225, 'COMPUTADOR DELL OPTIPLEX 5050SFF', 'Computador', 'BMG', '2024-06-16', 90),
(59, 83229, 'COMPUTADOR DELL OPTIPLEX 5050SFF', 'Computador', 'Ole - Treinamento', '2024-06-16', 90),
(60, 83237, 'COMPUTADOR DELL OPTIPLEX 5050SFF', 'Computador', 'Ole - Treinamento', '2024-06-16', 90),
(61, 75697, 'MONITOR DELL P2317H', 'Monitor', 'Ole - Treinamento', '2024-06-16', 20),
(62, 83242, 'COMPUTADOR DELL OPTIPLEX 5050SFF', 'Computador', 'Ole - Treinamento', '2024-06-16', 90),
(63, 73534, 'MONITOR DELL P2317H', 'Monitor', 'TI', '2024-06-16', 20),
(64, 73651, 'MONITOR DELL P2317H', 'Monitor', 'Ole - Treinamento', '2024-06-16', 20),
(65, 73766, 'MONITOR DELL P2317H', 'Monitor', 'BI', '2024-06-16', 20),
(66, 73984, 'MONITOR DELL P2317H', 'Monitor', 'Ole - Santander', '2024-06-16', 20),
(67, 74454, 'MONITOR DELL P2317H', 'Monitor', 'TI', '2024-06-16', 20),
(68, 74636, 'MONITOR DELL P2317H', 'Monitor', 'Ole - Treinamento', '2024-06-16', 20),
(69, 83286, 'COMPUTADOR DELL OPTIPLEX 5050SFF', 'Computador', 'Ole - Treinamento', '2024-06-16', 90),
(70, 101472, 'MONITOR DELL P2219H', 'Monitor', 'BI', '2024-06-16', 20),
(71, 62926, 'COMPUTADOR DELL OPTIPLEX 9020SFF', 'Computador', 'Ativos', '2024-06-16', 90),
(72, 60357, 'COMPUTADOR DELL OPTIPLEX 9020SFF', 'Computador', 'Monitoria', '2024-06-16', 90),
(73, 47602, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(74, 47336, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(75, 47335, 'MONITOR DELL P1913SB', 'Monitor', 'BMG', '2024-06-16', 10),
(76, 47334, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(77, 47033, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(78, 53716, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(79, 53715, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Mercantil', '2024-06-16', 90),
(80, 52050, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(81, 51136, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'TI', '2024-06-16', 90),
(82, 48738, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'BMG', '2024-06-16', 90),
(83, 48557, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(84, 47895, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(85, 47763, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(86, 47470, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(87, 47185, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'BMG', '2024-06-16', 90),
(88, 46771, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Mercantil', '2024-06-16', 90),
(89, 46767, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(90, 69435, 'COMPUTADOR DELL OPTIPLEX 7020SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(91, 71178, 'COMPUTADOR DELL OPTIPLEX 7020SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(92, 71885, 'COMPUTADOR DELL OPTIPLEX 9020SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(93, 46705, 'MONITOR DELL P1913SB', 'Monitor', 'Mercantil', '2024-06-16', 10),
(94, 49309, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(95, 57470, 'MONITOR DELL P1913SB', 'Monitor', 'TI', '2024-06-16', 10),
(96, 47609, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(97, 47792, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Laís Gonçalves', '2024-06-16', 90),
(98, 50597, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Mercantil', '2024-06-16', 90),
(99, 51476, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'TI', '2024-06-16', 90),
(100, 123482, 'MONITOR DELL P2419H', 'Monitor', 'Rodrigo', '2024-06-16', 40),
(101, 123487, 'MONITOR DELL P2419H', 'Monitor', 'Secretaria - Janete', '2024-06-16', 40),
(102, 123499, 'MONITOR DELL P2419H', 'Monitor', 'TI', '2024-06-16', 40),
(103, 46356, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'BMG', '2024-06-16', 90),
(104, 69548, 'COMPUTADOR DELL OPTIPLEX 7020SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(105, 48476, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(106, 49395, 'MONITOR DELL P1913SB', 'Monitor', 'Ativos', '2024-06-16', 10),
(107, 51039, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(108, 46597, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(109, 47203, 'MONITOR DELL P1913SB', 'Monitor', 'Laís filial 726', '2024-06-16', 10),
(110, 47308, 'MONITOR DELL P1913SB', 'Monitor', 'Ativos', '2024-06-16', 10),
(111, 47924, 'MONITOR DELL P1913SB', 'Monitor', 'Estoque - TI', '2024-06-16', 10),
(112, 47934, 'MONITOR DELL P1913SB', 'Monitor', 'Parana Banco', '2024-06-16', 10),
(113, 48036, 'MONITOR DELL P1913SB', 'Monitor', 'Parana Banco', '2024-06-16', 10),
(114, 34059, 'MONITOR DELL P1913SB', 'Monitor', 'Mercantil', '2024-06-16', 10),
(115, 48037, 'MONITOR DELL P1913SB', 'Monitor', 'Planejamento', '2024-06-16', 10),
(116, 51196, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(117, 57946, 'COMPUTADOR DELL OPTIPLEX 9020SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(118, 57965, 'COMPUTADOR DELL OPTIPLEX 9020SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(119, 58358, 'COMPUTADOR DELL OPTIPLEX 9020SFF', 'Computador', 'Monitoria', '2024-06-16', 90),
(120, 58666, 'COMPUTADOR DELL OPTIPLEX 9020SFF', 'Computador', 'Planejamento', '2024-06-16', 90),
(121, 58954, 'COMPUTADOR DELL OPTIPLEX 9020SFF', 'Computador', 'SALA DE REUNIÃO - 1500', '2024-06-16', 90),
(122, 48039, 'MONITOR DELL P1913SB', 'Monitor', 'Parana Banco', '2024-06-16', 10),
(123, 60358, 'COMPUTADOR DELL OPTIPLEX 9020SFF', 'Computador', 'BMG', '2024-06-16', 90),
(124, 50897, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Parana Banco', '2024-06-16', 90),
(125, 47359, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(126, 52685, 'MONITOR DELL P1913SB', 'Monitor', 'Sala de Reunião - 1500', '2024-06-16', 10),
(127, 52736, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(128, 53650, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(129, 53846, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(130, 58117, 'MONITOR DELL P1913SB', 'Monitor', 'Ole - Santander', '2024-06-16', 10),
(131, 58118, 'MONITOR DELL P1913SB', 'Monitor', 'Planejamento', '2024-06-16', 10),
(132, 49042, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Rodrigo Purri', '2024-06-16', 90),
(133, 47183, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'BMG', '2024-06-16', 90),
(134, 46850, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(135, 46865, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(136, 46947, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Parana Banco', '2024-06-16', 90),
(137, 46951, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(138, 47147, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(139, 47247, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Ole - Santander', '2024-06-16', 90),
(140, 46072, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Mercantil', '2024-06-16', 90),
(141, 105250, 'MONITOR DELL P2219H', 'Monitor', 'BI', '2024-06-16', 20),
(142, 171573, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Parana Banco', '2024-06-16', 90),
(143, 84374, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Parana Banco', '2024-09-11', 90),
(144, 84172, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Parana Banco', '2024-09-11', 90),
(145, 84772, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Parana Banco', '2024-09-11', 90),
(146, 81801, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Parana Banco', '2024-09-11', 90),
(147, 85065, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Parana Banco', '2024-09-11', 90),
(148, 85191, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Parana Banco', '2024-09-11', 90),
(149, 78814, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'BMG', '2024-09-11', 90),
(150, 85138, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'BMG', '2024-09-11', 90),
(151, 84966, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'BMG', '2024-09-11', 90),
(152, 84475, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Parana Banco', '2024-09-11', 90),
(153, 84804, 'COMPUTADOR DELL OPTIPLEX 9010SFF', 'Computador', 'Uso Digital', '2024-09-11', 90),
(154, 48683, 'MONITOR DELL P2219H', 'Monitor', 'Parana Banco', '2024-09-11', 10),
(155, 46407, 'MONITOR DELL P2219H', 'Monitor', 'Parana Banco', '2024-09-11', 10),
(156, 52929, 'MONITOR DELL P2219H', 'Monitor', 'Parana Banco', '2024-09-11', 10),
(157, 57550, 'MONITOR DELL P2219H', 'Monitor', 'Parana Banco', '2024-09-11', 10),
(158, 52690, 'MONITOR DELL P2219H', 'Monitor', 'Parana Banco', '2024-09-11', 10),
(159, 46315, 'MONITOR DELL P2219H', 'Monitor', 'Parana Banco', '2024-09-11', 10),
(160, 47408, 'MONITOR DELL P2219H', 'Monitor', 'Estoque - TI', '2024-09-11', 10),
(161, 46830, 'MONITOR DELL P2219H', 'Monitor', 'Estoque - TI', '2024-09-11', 10),
(162, 47303, 'MONITOR DELL P2219H', 'Monitor', 'Estoque - TI', '2024-09-11', 10),
(163, 48388, 'MONITOR DELL P2219H', 'Monitor', 'Estoque - TI', '2024-09-11', 10);

--
-- Acionadores `controle`
--
DROP TRIGGER IF EXISTS `registro_remove`;
DELIMITER $$
CREATE TRIGGER `registro_remove` AFTER DELETE ON `controle` FOR EACH ROW BEGIN
	INSERT INTO auditoria(id_produto, produto, tipo, descricao, data_remove)
    VALUES (OLD.emc_num, OLD.descricao, OLD.tipo, 
    CONCAT("O produto", OLD.descricao," foi exluído na data ",NOW()), NOW());
END
$$
DELIMITER ;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
