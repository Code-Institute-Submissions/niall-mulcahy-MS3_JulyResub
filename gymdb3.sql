-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 26, 2021 at 04:53 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 7.4.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gymdb`
--

-- --------------------------------------------------------


 DROP DATABASE IF EXISTS `gymdb`;

--
 CREATE DATABASE `gymdb`;
--
USE `gymdb`;


-- Table structure for table `barposition`
--

CREATE TABLE `barposition`
  `BarPositionId` tinyint(3) UNSIGNED NOT NULL,
  `BarPositionName` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `barposition`
--

INSERT INTO `barposition` (`BarPositionId`, `BarPositionName`) VALUES
(1, 'Low'),
(2, 'High'),
(3, 'Front'),
(4, 'Zercher');

-- --------------------------------------------------------

--
-- Table structure for table `bartype`
--

CREATE TABLE `bartype` (
  `BarTypeId` tinyint(3) UNSIGNED NOT NULL,
  `BarTypeName` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bartype`
--

INSERT INTO `bartype` (`BarTypeId`, `BarTypeName`) VALUES
(1, 'Stiff'),
(2, 'Squat'),
(3, 'Deadlift'),
(4, 'Trap'),
(5, 'Football'),
(6, 'Safety Squat');

-- --------------------------------------------------------

--
-- Table structure for table `deadliftstance`
--

CREATE TABLE `deadliftstance` (
  `DeadliftStanceId` tinyint(3) UNSIGNED NOT NULL,
  `DeadliftStanceName` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `deadliftstance`
--

INSERT INTO `deadliftstance` (`DeadliftStanceId`, `DeadliftStanceName`) VALUES
(1, 'Conventional'),
(2, 'Sumo');

-- --------------------------------------------------------

--
-- Table structure for table `exercise`
--

CREATE TABLE `exercise` (
  `ExerciseId` int(10) UNSIGNED NOT NULL,
  `SessionId` int(10) UNSIGNED NOT NULL,
  `ExerciseTypeId` int(10) UNSIGNED NOT NULL,
  `StanceWidthId` tinyint(3) UNSIGNED DEFAULT NULL,
  `GripWidthId` tinyint(3) UNSIGNED DEFAULT NULL,
  `BarPositionId` tinyint(3) UNSIGNED DEFAULT NULL,
  `BarTypeId` tinyint(3) UNSIGNED DEFAULT NULL,
  `Belt` tinyint(4) DEFAULT NULL,
  `TempoId` smallint(5) UNSIGNED DEFAULT NULL,
  `Pause` tinyint(4) DEFAULT NULL,
  `PinId` int(3) UNSIGNED DEFAULT NULL,
  `DeadliftStanceId` tinyint(3) UNSIGNED DEFAULT NULL,
  `SnatchGrip` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `exercisetype`
--

CREATE TABLE `exercisetype` (
  `ExerciseTypeId` int(10) UNSIGNED NOT NULL,
  `ExerciseTypeName` varchar(45) NOT NULL,
  `DisplayOrder` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `exercisetype`
--

INSERT INTO `exercisetype` (`ExerciseTypeId`, `ExerciseTypeName`, `DisplayOrder`) VALUES
(1, 'Squat', 1),
(2, 'Bench Press', 1),
(3, 'Deadlift', 1),
(4, 'Chin Up', 4),
(5, 'Bent Over Row', 4),
(6, 'Dumbbell Press', 2),
(7, 'Incline Press', 2),
(8, 'Romanian Deadlift', 5),
(9, 'Stiff Legged Deadlift', 5),
(10, 'Shoulder Press', 2),
(11, 'Bicep Curls', 4),
(12, 'Lateral Raises', 2),
(13, 'Rear Delt Flies', 4),
(14, 'Chest Flies', 2),
(15, 'Tricep Extensions', 2),
(16, 'Bulgarian Split Squats', 3),
(17, 'Hamstring Curls', 5),
(18, 'Leg Extensions', 3);

-- --------------------------------------------------------

--
-- Table structure for table `gripwidth`
--

CREATE TABLE `gripwidth` (
  `GripWidthId` tinyint(3) UNSIGNED NOT NULL,
  `GripWidthName` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `gripwidth`
--

INSERT INTO `gripwidth` (`GripWidthId`, `GripWidthName`) VALUES
(1, 'Competition'),
(2, 'Close Grip'),
(3, 'Wide Grip');

-- --------------------------------------------------------

--
-- Table structure for table `pin`
--

CREATE TABLE `pin` (
  `PinId` int(10) UNSIGNED NOT NULL,
  `PinHeight` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `pin`
--

INSERT INTO `pin` (`PinId`, `PinHeight`) VALUES
(1, 'Low'),
(2, 'Medium'),
(3, 'High');

-- --------------------------------------------------------

--
-- Table structure for table `session`
--

CREATE TABLE `session` (
  `SessionId` int(10) UNSIGNED NOT NULL,
  `User` int(10) UNSIGNED NOT NULL,
  `SessionDate` date NOT NULL,
  `SessionTime` int(10) UNSIGNED NOT NULL,
  `SessionName` varchar(50) DEFAULT NULL,
  `SessionRPE` tinyint(2) UNSIGNED NOT NULL,
  `SessionAU` smallint(4) GENERATED ALWAYS AS (`SessionTime` * `SessionRPE`) VIRTUAL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `session`
--

INSERT INTO `session` (`SessionId`, `User`, `SessionDate`, `SessionTime`, `SessionName`, `SessionRPE`) VALUES
(1, 1, '0000-00-00', 120, 'Test', 5);

-- --------------------------------------------------------

--
-- Table structure for table `sets`
--

CREATE TABLE `sets` (
  `SetId` int(10) UNSIGNED NOT NULL,
  `ExerciseId` int(10) UNSIGNED NOT NULL,
  `Reps` int(10) UNSIGNED NOT NULL,
  `Weight` decimal(4,1) UNSIGNED NOT NULL,
  `RPE` decimal(4,1) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `stancewidth`
--

CREATE TABLE `stancewidth` (
  `StanceWidthId` tinyint(3) UNSIGNED NOT NULL,
  `StanceWidthName` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `stancewidth`
--

INSERT INTO `stancewidth` (`StanceWidthId`, `StanceWidthName`) VALUES
(1, 'Competition'),
(2, 'Narrow'),
(3, 'Wide');

-- --------------------------------------------------------

--
-- Table structure for table `tempo`
--

CREATE TABLE `tempo` (
  `TempoId` smallint(5) UNSIGNED NOT NULL,
  `TempoType` char(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tempo`
--

INSERT INTO `tempo` (`TempoId`, `TempoType`) VALUES
(1, '210'),
(2, '310'),
(3, '320'),
(4, '510'),
(5, '303');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `UserId` int(10) UNSIGNED NOT NULL,
  `FirstName` varchar(25) NOT NULL,
  `LastName` varchar(25) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Username` varchar(45) NOT NULL,
  `Password` char(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`UserId`, `FirstName`, `LastName`, `Email`, `Username`, `Password`) VALUES
(1, 'Irene', 'McNamara', 'irenemcnamara@gmail.com', 'irene', '123456789');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `barposition`
--
ALTER TABLE `barposition`
  ADD PRIMARY KEY (`BarPositionId`);

--
-- Indexes for table `bartype`
--
ALTER TABLE `bartype`
  ADD PRIMARY KEY (`BarTypeId`);

--
-- Indexes for table `deadliftstance`
--
ALTER TABLE `deadliftstance`
  ADD PRIMARY KEY (`DeadliftStanceId`);

--
-- Indexes for table `exercise`
--
ALTER TABLE `exercise`
  ADD PRIMARY KEY (`ExerciseId`),
  ADD KEY `fk_session` (`SessionId`),
  ADD KEY `fk_extype` (`ExerciseTypeId`),
  ADD KEY `fk_stance` (`StanceWidthId`),
  ADD KEY `fk_grip` (`GripWidthId`),
  ADD KEY `fk_barpos` (`BarPositionId`),
  ADD KEY `fk_btype` (`BarTypeId`),
  ADD KEY `fk_tempo` (`TempoId`),
  ADD KEY `fk_pin` (`PinId`);

--
-- Indexes for table `exercisetype`
--
ALTER TABLE `exercisetype`
  ADD PRIMARY KEY (`ExerciseTypeId`);

--
-- Indexes for table `gripwidth`
--
ALTER TABLE `gripwidth`
  ADD PRIMARY KEY (`GripWidthId`);

--
-- Indexes for table `pin`
--
ALTER TABLE `pin`
  ADD PRIMARY KEY (`PinId`);

--
-- Indexes for table `session`
--
ALTER TABLE `session`
  ADD PRIMARY KEY (`SessionId`),
  ADD KEY `fk_user` (`User`);

--
-- Indexes for table `sets`
--
ALTER TABLE `sets`
  ADD PRIMARY KEY (`SetId`),
  ADD KEY `fk_exercise` (`ExerciseId`);

--
-- Indexes for table `stancewidth`
--
ALTER TABLE `stancewidth`
  ADD PRIMARY KEY (`StanceWidthId`);

--
-- Indexes for table `tempo`
--
ALTER TABLE `tempo`
  ADD PRIMARY KEY (`TempoId`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`UserId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `barposition`
--
ALTER TABLE `barposition`
  MODIFY `BarPositionId` tinyint(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `bartype`
--
ALTER TABLE `bartype`
  MODIFY `BarTypeId` tinyint(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `deadliftstance`
--
ALTER TABLE `deadliftstance`
  MODIFY `DeadliftStanceId` tinyint(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `exercise`
--
ALTER TABLE `exercise`
  MODIFY `ExerciseId` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `exercisetype`
--
ALTER TABLE `exercisetype`
  MODIFY `ExerciseTypeId` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `gripwidth`
--
ALTER TABLE `gripwidth`
  MODIFY `GripWidthId` tinyint(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `pin`
--
ALTER TABLE `pin`
  MODIFY `PinId` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `session`
--
ALTER TABLE `session`
  MODIFY `SessionId` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `sets`
--
ALTER TABLE `sets`
  MODIFY `SetId` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `stancewidth`
--
ALTER TABLE `stancewidth`
  MODIFY `StanceWidthId` tinyint(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tempo`
--
ALTER TABLE `tempo`
  MODIFY `TempoId` smallint(5) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `UserId` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `exercise`
--
ALTER TABLE `exercise`
  ADD CONSTRAINT `fk_barpos` FOREIGN KEY (`BarPositionId`) REFERENCES `barposition` (`BarPositionId`),
  ADD CONSTRAINT `fk_btype` FOREIGN KEY (`BarTypeId`) REFERENCES `bartype` (`BarTypeId`),
  ADD CONSTRAINT `fk_extype` FOREIGN KEY (`ExerciseTypeId`) REFERENCES `exercisetype` (`ExerciseTypeId`),
  ADD CONSTRAINT `fk_grip` FOREIGN KEY (`GripWidthId`) REFERENCES `gripwidth` (`GripWidthId`),
  ADD CONSTRAINT `fk_pin` FOREIGN KEY (`PinId`) REFERENCES `pin` (`PinId`),
  ADD CONSTRAINT `fk_session` FOREIGN KEY (`SessionId`) REFERENCES `session` (`SessionId`),
  ADD CONSTRAINT `fk_stance` FOREIGN KEY (`StanceWidthId`) REFERENCES `stancewidth` (`StanceWidthId`),
  ADD CONSTRAINT `fk_tempo` FOREIGN KEY (`TempoId`) REFERENCES `tempo` (`TempoId`);

--
-- Constraints for table `session`
--
ALTER TABLE `session`
  ADD CONSTRAINT `fk_user` FOREIGN KEY (`User`) REFERENCES `user` (`UserId`);

--
-- Constraints for table `sets`
--
ALTER TABLE `sets`
  ADD CONSTRAINT `fk_exercise` FOREIGN KEY (`ExerciseId`) REFERENCES `exercise` (`ExerciseId`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
