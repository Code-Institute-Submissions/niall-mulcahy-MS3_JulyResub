USE `gymdb`;
CREATE 
     OR REPLACE ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `gymdb`.`exerciseDisplay` AS
    SELECT 
        `e`.`SessionId` AS `SessionId`,
        `e`.`ExerciseId` AS `ExerciseId`,
        COALESCE(`a`.`BarTypeName`, '') AS `BarTypeName`,
        COALESCE(`b`.`BarPositionName`, '') AS `BarPositionName`,
        COALESCE(`t`.`ExerciseTypeName`, '') AS `ExerciseTypeName`,
        COALESCE(`p`.`PinHeight`, '') AS `PinHeight`,
        COALESCE(`e`.`SnatchGrip`, '') AS `SnatchGrip`,
        COALESCE(`e`.`Pause`, '') AS `Pause`,
        COALESCE(`e`.`Belt`, '') AS `Belt`,
        COALESCE(`g`.`GripWidthName`, '') AS `GripWidthName`,
        COALESCE(`d`.`DeadliftStanceName`, '') AS `DeadliftStanceName`,
        COALESCE(`o`.`TempoType`, '') AS `TempoType`,
        COALESCE(`s`.`StanceWidthName`, '') AS `StanceWidthName`
    FROM
        ((((((((`gymdb`.`exercise` `e`
        LEFT JOIN `gymdb`.`bartype` `a` ON (`e`.`BarTypeId` = `a`.`BarTypeId`))
        LEFT JOIN `gymdb`.`barposition` `b` ON (`e`.`BarPositionId` = `b`.`BarPositionId`))
        LEFT JOIN `gymdb`.`exercisetype` `t` ON (`e`.`ExerciseTypeId` = `t`.`ExerciseTypeId`))
        LEFT JOIN `gymdb`.`pin` `p` ON (`e`.`PinId` = `p`.`PinId`))
        LEFT JOIN `gymdb`.`gripwidth` `g` ON (`e`.`GripWidthId` = `g`.`GripWidthId`))
        LEFT JOIN `gymdb`.`deadliftstance` `d` ON (`e`.`DeadliftStanceId` = `d`.`DeadliftStanceId`))
        LEFT JOIN `gymdb`.`tempo` `o` ON (`e`.`TempoId` = `o`.`TempoId`))
        LEFT JOIN `gymdb`.`stancewidth` `s` ON (`e`.`StanceWidthId` = `s`.`StanceWidthId`));
USE `gymdb`;
CREATE 
     OR REPLACE ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `gymdb`.`display_exercise` AS
    SELECT 
        `e`.`SessionId` AS `SessionId`,
        `e`.`ExerciseId` AS `ExerciseId`,
        COALESCE(`a`.`BarTypeName`, '') AS `BarTypeName`,
        COALESCE(`b`.`BarPositionName`, '') AS `BarPositionName`,
        COALESCE(`t`.`ExerciseTypeName`, '') AS `ExerciseTypeName`,
        COALESCE(`p`.`PinHeight`, '') AS `PinHeight`,
        COALESCE(`e`.`SnatchGrip`, '') AS `SnatchGrip`,
        COALESCE(`e`.`Pause`, '') AS `Pause`,
        COALESCE(`e`.`Belt`, '') AS `Belt`,
        COALESCE(`g`.`GripWidthName`, '') AS `GripWidthName`,
        COALESCE(`d`.`DeadliftStanceName`, '') AS `DeadliftStanceName`,
        COALESCE(`o`.`TempoType`, '') AS `TempoType`,
        COALESCE(`s`.`StanceWidthName`, '') AS `StanceWidthName`
    FROM
        ((((((((`gymdb`.`exercise` `e`
        LEFT JOIN `gymdb`.`bartype` `a` ON (`e`.`BarTypeId` = `a`.`BarTypeId`))
        LEFT JOIN `gymdb`.`barposition` `b` ON (`e`.`BarPositionId` = `b`.`BarPositionId`))
        LEFT JOIN `gymdb`.`exercisetype` `t` ON (`e`.`ExerciseTypeId` = `t`.`ExerciseTypeId`))
        LEFT JOIN `gymdb`.`pin` `p` ON (`e`.`PinId` = `p`.`PinId`))
        LEFT JOIN `gymdb`.`gripwidth` `g` ON (`e`.`GripWidthId` = `g`.`GripWidthId`))
        LEFT JOIN `gymdb`.`deadliftstance` `d` ON (`e`.`DeadliftStanceId` = `d`.`DeadliftStanceId`))
        LEFT JOIN `gymdb`.`tempo` `o` ON (`e`.`TempoId` = `o`.`TempoId`))
        LEFT JOIN `gymdb`.`stancewidth` `s` ON (`e`.`StanceWidthId` = `s`.`StanceWidthId`));
