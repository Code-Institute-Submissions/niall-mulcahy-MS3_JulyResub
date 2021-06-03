SELECT SessionId, ExerciseId, 
CONCAT(ExerciseTypeName, 
IF(BarTypeName is not null and BarTypeName != '', CONCAT(', ', BarTypeName), ''), 
IF(BarPositionName is not null and BarPositionName != '', CONCAT(', ', BarPositionName), ''), 
IF(PinHeight is not null and PinHeight <> '' , CONCAT(', ', PinHeight), ''), 
IF(SnatchGrip = 1,', Snatch Grip', ''),
IF(Belt is null or Belt = '','',IF(Belt = 0, ', Beltless' , ', With Belt')),
IF(GripWidthName is not null and GripWidthName != '', CONCAT(', ', GripWidthName), ''),
IF(StanceWidthName is not null and StanceWidthName != '', CONCAT(', ', StanceWidthName), ''),
IF(Pause is not null and Pause <> '' , CONCAT(', ', Pause), ''),

TempoType) as ExerciseTextualDescription
 FROM gymdb.display_exercise;