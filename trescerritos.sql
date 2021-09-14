-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 14-09-2021 a las 16:02:29
-- Versión del servidor: 5.7.31
-- Versión de PHP: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `trescerritos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `brokers`
--

DROP TABLE IF EXISTS `brokers`;
CREATE TABLE IF NOT EXISTS `brokers` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Apellido` varchar(50) NOT NULL,
  `Direccion` varchar(100) NOT NULL,
  `Telefono` varchar(50) NOT NULL,
  `Correo` varchar(100) NOT NULL,
  `Certificado_habilitacion` varchar(100) NOT NULL,
  `Cuit` varchar(50) NOT NULL,
  `Activo` varchar(2) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `brokers`
--

INSERT INTO `brokers` (`Id`, `Nombre`, `Apellido`, `Direccion`, `Telefono`, `Correo`, `Certificado_habilitacion`, `Cuit`, `Activo`) VALUES
(1, 'Manuel Gustavo', 'Gomez', 'Italia 6458', '3814789123', 'Manuel@email.com', 'qwe2154-5', '20-51432583-7', 'Si'),
(2, 'Javier', 'Alvarez', 'Santa Fe 6842', '38154224828', 'javier@email.com', '1231173-ff', '26-242457426-6', 'Si');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `camiones`
--

DROP TABLE IF EXISTS `camiones`;
CREATE TABLE IF NOT EXISTS `camiones` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Chofer` varchar(100) NOT NULL,
  `DNI` int(11) NOT NULL,
  `Telefono` varchar(50) NOT NULL,
  `Direccion` varchar(100) NOT NULL,
  `Marca` varchar(50) NOT NULL,
  `Patente_chasis` varchar(20) NOT NULL,
  `Patente_semi_acoplado` varchar(20) NOT NULL,
  `Detalle_camion` varchar(500) NOT NULL,
  `Activo` varchar(2) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `camiones`
--

INSERT INTO `camiones` (`Id`, `Chofer`, `DNI`, `Telefono`, `Direccion`, `Marca`, `Patente_chasis`, `Patente_semi_acoplado`, `Detalle_camion`, `Activo`) VALUES
(1, 'Santiago Mendez', 30123456, '3816666444', 'Esquiu 543', 'Escania', 'AC-666-DC', 'AC-777-DC', 'Es de color Rojo', 'Si'),
(2, 'Hector De Gaetano', 33430082, '3816452125', 'SAN MIGUEL DE TUCUMAN', 'ESCANIA 410', 'AB608XL', 'OLF2798', 'Escania color rojo termo blanco insignia VPM', 'Si'),
(3, 'Lucas Castro', 30123887, '3815728964', 'calle 3', 'Mercedes 123', 'AA111QL', 'ZSE458', 'Camion grande color negro y rojo', 'Si');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

DROP TABLE IF EXISTS `clientes`;
CREATE TABLE IF NOT EXISTS `clientes` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Apellido` varchar(50) NOT NULL,
  `Direccion` varchar(100) NOT NULL,
  `Telefono` varchar(50) NOT NULL,
  `Correo` varchar(50) NOT NULL,
  `Cuit` varchar(30) NOT NULL,
  `Referente` varchar(50) NOT NULL,
  `Razon_social` varchar(50) NOT NULL,
  `Habilitacion_senasa` varchar(50) NOT NULL,
  `Activo` varchar(2) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`Id`, `Nombre`, `Apellido`, `Direccion`, `Telefono`, `Correo`, `Cuit`, `Referente`, `Razon_social`, `Habilitacion_senasa`, `Activo`) VALUES
(1, 'Pedro', 'Perez', 'España 1423', '3816212121', 'prueba@email.com', '20-12123123-8', 'Miguel Castillo', 'Algo SRL', '12354-asd-5', 'Si'),
(3, 'Carlos', 'Mamani', 'Laprida 758', '3816584712', 'carlos@gmail.com', '20-31205789-6', 'Santiago Mendez', 'Blue SRL', 'Bgre67-17', 'Si');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `importaciones_compra`
--

DROP TABLE IF EXISTS `importaciones_compra`;
CREATE TABLE IF NOT EXISTS `importaciones_compra` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre_empresa` varchar(60) NOT NULL,
  `Nro_factura` varchar(50) NOT NULL,
  `Telefono` varchar(30) NOT NULL,
  `Localidad` varchar(60) NOT NULL,
  `Pais` varchar(30) NOT NULL,
  `Cliente` int(11) NOT NULL,
  `Nro_transaccion` varchar(50) NOT NULL,
  `Nro_remito` varchar(50) NOT NULL,
  `Broker` int(11) NOT NULL,
  `Precio_dolar_transaccion` float NOT NULL,
  `Producto` varchar(60) NOT NULL,
  `Precio_unitario_USD` float NOT NULL,
  `Precio_flete_USD` float NOT NULL,
  `Precio_flete_unitario_USD` float NOT NULL,
  `Gasto_despacho_USD` float NOT NULL,
  `Gasto_despacho_unitario_USD` float NOT NULL,
  `Fecha_emision_factura` date NOT NULL,
  `Fecha_ingreso_pais` date NOT NULL,
  `Detalle_pago` varchar(50) NOT NULL,
  `Camion` int(11) NOT NULL,
  `Cantidad_bulto` int(11) NOT NULL,
  `Precio_unitario_ARS` float NOT NULL,
  `Precio_flete_ARS` float NOT NULL,
  `Precio_flete_unitario_ARS` float NOT NULL,
  `Gasto_despacho_ARS` float NOT NULL,
  `Gasto_despacho_unitario_ARS` float NOT NULL,
  `Fecha_deposito` date NOT NULL,
  `Observaciones` varchar(2000) NOT NULL,
  `CRT` varchar(50) NOT NULL,
  `Nro_MIC` varchar(50) NOT NULL,
  `Nro_CUVE` varchar(50) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `importaciones_compra`
--

INSERT INTO `importaciones_compra` (`Id`, `Nombre_empresa`, `Nro_factura`, `Telefono`, `Localidad`, `Pais`, `Cliente`, `Nro_transaccion`, `Nro_remito`, `Broker`, `Precio_dolar_transaccion`, `Producto`, `Precio_unitario_USD`, `Precio_flete_USD`, `Precio_flete_unitario_USD`, `Gasto_despacho_USD`, `Gasto_despacho_unitario_USD`, `Fecha_emision_factura`, `Fecha_ingreso_pais`, `Detalle_pago`, `Camion`, `Cantidad_bulto`, `Precio_unitario_ARS`, `Precio_flete_ARS`, `Precio_flete_unitario_ARS`, `Gasto_despacho_ARS`, `Gasto_despacho_unitario_ARS`, `Fecha_deposito`, `Observaciones`, `CRT`, `Nro_MIC`, `Nro_CUVE`) VALUES
(1, 'A&T', '002-00008459', '15463541831', 'TEMBIAPORA', 'PARAGUAY', 2, '32154', '021626+5135', 1, 8.36, 'BANANA ', 8, 1350, 3, 1500, 1.5, '2021-10-16', '2021-10-19', 'EFECTIVO  X BCO', 1, 1050, 900, 130000, 130, 210000, 210, '2021-10-22', 'LLEGARON 1050 CAJAS DE BANANAS CON PROMEDIO DE 22.5 KG DE FRUTA  DE LOS CUALES LLEGARON 150 MANCHADAS Y 50 ABANDERADAS ', '00000000513216594563', '0000023154156323561', '000000516531235435');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `importaciones_forma_de_pago`
--

DROP TABLE IF EXISTS `importaciones_forma_de_pago`;
CREATE TABLE IF NOT EXISTS `importaciones_forma_de_pago` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Id_importacion` int(11) NOT NULL,
  `Tipo` varchar(30) NOT NULL,
  `Monto` float NOT NULL,
  `Fecha` date NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `importaciones_forma_de_pago`
--

INSERT INTO `importaciones_forma_de_pago` (`Id`, `Id_importacion`, `Tipo`, `Monto`, `Fecha`) VALUES
(1, 2, 'PARCIAL EN EFECTIVO', 500000, '2021-10-22'),
(2, 2, 'PARCIAL EN EFECTIVO', 300000, '2021-10-23'),
(3, 2, 'PARCIAL EN EFECTIVO', 400000, '2021-10-25');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `importaciones_venta`
--

DROP TABLE IF EXISTS `importaciones_venta`;
CREATE TABLE IF NOT EXISTS `importaciones_venta` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Cliente` int(11) NOT NULL,
  `Nro_factura` varchar(50) NOT NULL,
  `Telefono` varchar(30) NOT NULL,
  `Precio_dolar_transaccion` float NOT NULL,
  `Producto` varchar(60) NOT NULL,
  `Precio_bulto` float NOT NULL,
  `Precio_total` float NOT NULL,
  `Nro_transaccion` varchar(30) NOT NULL,
  `Importe_compra` float NOT NULL,
  `Nro_remito` varchar(30) NOT NULL,
  `Pais` varchar(30) NOT NULL,
  `Provincia` varchar(60) NOT NULL,
  `Localidad` varchar(60) NOT NULL,
  `Establecimiento` varchar(60) NOT NULL,
  `Observaciones` varchar(1200) NOT NULL,
  `Camion` int(11) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `importaciones_venta`
--

INSERT INTO `importaciones_venta` (`Id`, `Cliente`, `Nro_factura`, `Telefono`, `Precio_dolar_transaccion`, `Producto`, `Precio_bulto`, `Precio_total`, `Nro_transaccion`, `Importe_compra`, `Nro_remito`, `Pais`, `Provincia`, `Localidad`, `Establecimiento`, `Observaciones`, `Camion`) VALUES
(1, 1, '0012-31265465321', '38152565465', 105, 'BANANA', 1200, 1200000, '123154', 1200000, '00000.-0002161515', 'ARGENTINA', 'TUCUMAN', 'YERBA BUENA', 'MERCOFRUT', 'Observaciones de una venta de importaciones', 3),
(2, 1, '0012-31265465321', '38152565465', 105, 'MANZANAS', 1200, 1200000, '314455', 1200000, '00000.-0001235235', 'ARGENTINA', 'TUCUMAN', 'YERBA BUENA', 'MERCOFRUT', 'Observaciones de una venta de importaciones', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mercado_interno_compra`
--

DROP TABLE IF EXISTS `mercado_interno_compra`;
CREATE TABLE IF NOT EXISTS `mercado_interno_compra` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre_empresa` varchar(50) NOT NULL,
  `Nro_factura` varchar(50) NOT NULL,
  `Telefono` varchar(30) NOT NULL,
  `Pais` varchar(30) NOT NULL,
  `Provincia` varchar(30) NOT NULL,
  `Cliente` int(11) NOT NULL,
  `Nro_transaccion` varchar(50) NOT NULL,
  `Nro_remito` varchar(50) NOT NULL,
  `Producto` varchar(60) NOT NULL,
  `Fecha_emision_factura` date NOT NULL,
  `Detalle_pago` varchar(60) NOT NULL,
  `Camion` int(11) NOT NULL,
  `Cantidad_bulto` int(11) NOT NULL,
  `Precio_unitario_ARS` float NOT NULL,
  `Precio_flete_ARS` float NOT NULL,
  `Precio_flete_unitario_ARS` float NOT NULL,
  `Observaciones` varchar(2000) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `mercado_interno_compra`
--

INSERT INTO `mercado_interno_compra` (`Id`, `Nombre_empresa`, `Nro_factura`, `Telefono`, `Pais`, `Provincia`, `Cliente`, `Nro_transaccion`, `Nro_remito`, `Producto`, `Fecha_emision_factura`, `Detalle_pago`, `Camion`, `Cantidad_bulto`, `Precio_unitario_ARS`, `Precio_flete_ARS`, `Precio_flete_unitario_ARS`, `Observaciones`) VALUES
(1, 'AGROPECUARIA ARROYO SECO ', '0002-0326216549821', '3816+456312', 'Argentina', 'Tucuman', 1, '5', '25151-32154685', 'SANDIA', '2021-10-16', 'EFECTIVO', 2, 4200, 124, 226, 13, 'Observaciones de una compra de mercado interno'),
(3, 'Empresa 123', '0002-0326216549821', '3816+456312', 'Argentina', 'Tucuman', 1, '5', '25151-32154685', 'SANDIA', '2021-10-16', 'EFECTIVO', 2, 4200, 123.6, 226, 12.8, 'Observaciones de una compra de mercado interno');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mercado_interno_venta`
--

DROP TABLE IF EXISTS `mercado_interno_venta`;
CREATE TABLE IF NOT EXISTS `mercado_interno_venta` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Cliente` int(11) NOT NULL,
  `Telefono` varchar(50) NOT NULL,
  `Provincia` varchar(50) NOT NULL,
  `Producto` varchar(60) NOT NULL,
  `Precio_por_bulto` float NOT NULL,
  `Cantidad_por_bulto` int(11) NOT NULL,
  `Precio_por_KG` float NOT NULL,
  `Precio_total` float NOT NULL,
  `Forma_de_pago` varchar(50) NOT NULL,
  `Operacion` varchar(50) NOT NULL,
  `Nro_transaccion` varchar(50) NOT NULL,
  `Nro_factura` varchar(50) NOT NULL,
  `Importe_compra` float NOT NULL,
  `Nro_remito` varchar(50) NOT NULL,
  `Establecimiento` varchar(60) NOT NULL,
  `Observaciones` varchar(2000) NOT NULL,
  `Camion` int(11) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `mercado_interno_venta`
--

INSERT INTO `mercado_interno_venta` (`Id`, `Cliente`, `Telefono`, `Provincia`, `Producto`, `Precio_por_bulto`, `Cantidad_por_bulto`, `Precio_por_KG`, `Precio_total`, `Forma_de_pago`, `Operacion`, `Nro_transaccion`, `Nro_factura`, `Importe_compra`, `Nro_remito`, `Establecimiento`, `Observaciones`, `Camion`) VALUES
(1, 1, '1233532251', 'Tucuman', 'Bananas', 123.45, 45, 0, 5555.25, 'Efectivo', '12', '134112', '3453451-345', 5555.25, '2342', 'Las palmeras', 'Observacion de una Venta en Mercado Interno', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mercado_int_compra_depositos`
--

DROP TABLE IF EXISTS `mercado_int_compra_depositos`;
CREATE TABLE IF NOT EXISTS `mercado_int_compra_depositos` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Id_mercado_int_compra` int(11) NOT NULL,
  `Monto` float NOT NULL,
  `Fecha` date NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `mercado_int_compra_depositos`
--

INSERT INTO `mercado_int_compra_depositos` (`Id`, `Id_mercado_int_compra`, `Monto`, `Fecha`) VALUES
(1, 1, 50000, '2021-12-10'),
(2, 1, 3000, '2021-10-17'),
(3, 2, 50000, '2021-12-10'),
(4, 2, 3000, '2021-10-17'),
(5, 3, 50000, '2021-12-10'),
(6, 3, 3000, '2021-10-17');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
