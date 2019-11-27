public void RegEditChecker()
        {
            /*//////////////////////////////////
          * To perform this test manually on a GC:
          * Start > Type regedit > Press "Enter"
          * Expected: Blocked by administrator
          */ //////////////////////////////////

            // TODO Update the verification process to: Confirm Local Group Policy setting directly via gpedit.msc

            testName = "Regedit Access";
            actualResult = "User has access to the Registry Editor";
            expectedResult = "User is blocked from accessing Registry Editor";
            string closeProgram = "regedit";
            notRunFlag = true;

            //Simulate Key Press Left Windows Key 
            InputSimulator.SimulateKeyPress( VirtualKeyCode.LWIN );

            //Sleep briefly
            Thread.Sleep( 2000 );

            //Send Regedit command
            SendKeys.SendWait( "r" );

            //Sleep briefly
            Thread.Sleep( 50 );

            //Send Regedit command
            SendKeys.SendWait( "e" );

            //Sleep briefly
            Thread.Sleep( 50 );

            //Send Regedit command
            SendKeys.SendWait( "g" );

            //Sleep briefly
            Thread.Sleep( 50 );

            //Send Regedit command
            SendKeys.SendWait( "e" );

            //Sleep briefly
            Thread.Sleep( 50 );

            //Send Regedit command
            SendKeys.SendWait( "d" );

            //Sleep briefly
            Thread.Sleep( 50 );

            //Send Regedit command
            SendKeys.SendWait( "i" );

            //Sleep briefly
            Thread.Sleep( 50 );

            //Send Regedit command
            SendKeys.SendWait( "t" );

            //Sleep briefly
            Thread.Sleep( 50 );

            //Send Regedit command
            SendKeys.SendWait( "{ENTER}" );

            //Sleep briefly
            Thread.Sleep( 2000 );

            // Send ESC; the Error window will close, but the Real Window will not
            SendKeys.SendWait( "{ESC}" );

            //Sleep briefly
            Thread.Sleep( 2000 );

            WaitToClose:
            Thread.Sleep( 10 );

            foreach ( Process chkProcess in Process.GetProcesses() )
            {
                if ( chkProcess.ProcessName.Contains( closeProgram ) )
                {
                    //Fail scenario output
                    if ( notRunFlag )
                    {
                        FailedTests();
                    }
                    try
                    {
                        int i = 0;
                        i++;
                        chkProcess.Kill();
                        //make this process escape if it takes too long
                        if ( i == 10 )
                        {
                            Console.WriteLine(
                                    "Closing" + closeProgram +
                                    "took too long -- please close manually and run this program again." );
                            break;
                        }
                        goto WaitToClose;
                    }
                    catch ( Exception )
                    {
                        if ( notRunFlag )
                        {
                            NotRun();
                        }
                        Console.WriteLine(
                                "Closing" + closeProgram +
                                "took too long. Please close manually and run this program again." );
                    }
                }
            }
            if ( notRunFlag )
            {
                PassedTests();
            }
        }