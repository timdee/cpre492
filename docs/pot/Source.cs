    public class MCP4131
    {
        SPI.Configuration MCP4131_Config;
        SPI MCP4131_SPI;
        public byte Tcon_Reg; //TCON register
        public byte Status_Reg; //Status Register
        public byte Wiper_Reg; //Wiper Register

        public MCP4131(Cpu.Pin cs_pin, SPI.SPI_module mod)
        {
            MCP4131_Config = new SPI.Configuration(cs_pin, false, 0, 0, false, true, 800, mod);
            MCP4131_SPI = new SPI(MCP4131_Config);
        }

        private byte transfer(byte cmd)
        {
            // Wrapper to use transfer from the original C source code Smiley
            byte[] rx = new byte[1];
            MCP4131_SPI.WriteRead(new byte[1] { cmd }, rx);
            return rx[0];
        }

        private byte double_transfer(byte cmd, byte ext_cmd, out byte register_value)
        {
            byte[] rx = new byte[2];
            MCP4131_SPI.WriteRead(new byte[2] { cmd, ext_cmd }, rx);
            register_value = rx[1];
            return rx[0];
        }

        public bool increment()
        {
            //  send in the address and value via SPI:
            byte ret1 = (byte)(0x02 & transfer(0x06));
            return (ret1 == 0);
            //Needs bit 1 for error checking, Bit 2 inc
        }

        public bool decrement()
        {
            //  send in the address and value via SPI:
            byte ret1 = (byte)(0x02 & transfer(0x0A));
            //Needs bit 1 for error checking, Bit 3 Dec
            return (ret1 == 0);
        }

        public bool readTCON()
        {
            //  send in the address and value via SPI:
            byte ret1 = (byte)(0x02 & double_transfer(0x4F, 0xFF, out Tcon_Reg));
            //At memory address 4 we read
            return (ret1 == 0);
        }

        public bool initTCON()
        {
            //Turns on Wiper 0, connects the terminals to the resistor network.
            byte ret2;
            byte ret1 = (byte)(0x02 & double_transfer(0x43, 0x0F, out ret2));
            return (ret1 == 0);//error checking True if there is some.
        }

        public bool readStatus()
        {
            //  send in the address and value via SPI:
            byte ret1 = (byte)(0x02 & double_transfer(0x5F, 0xFF, out Status_Reg));
            return (ret1 == 0);//error checking True if there is some.
        }

        public bool setTap(int value)
        {
            //  send in the address and value via SPI:
            byte h = (byte)(0x03 & (value >> 8));
            byte l = (byte)(0x00FF & value);
            byte ret2;
            h = (byte)(h | 0x02); //make sure the error checking bit is high
            byte ret1 = (byte)(0x02 & double_transfer(h, l, out ret2)); //we only want the error bit
            readTap();
            return (ret1 == 0);//error checking True if there is some.
        }

        public bool readTap()
        {
            byte ret1 = (byte)(0x02 & double_transfer(0x0F, 0xFF, out Wiper_Reg)); //Read Wiper 0, check error
            return (ret1 == 0);//error checking True if there is some.
        }

    }
