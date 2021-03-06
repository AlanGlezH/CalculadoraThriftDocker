#
# Autogenerated by Thrift Compiler (0.13.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
all_structs = []


class Iface(object):
    def Sumar(self, numeroUno, numeroDos):
        """
        Parameters:
         - numeroUno
         - numeroDos

        """
        pass

    def Restar(self, numeroUno, numeroDos):
        """
        Parameters:
         - numeroUno
         - numeroDos

        """
        pass

    def Multiplicar(self, numeroUno, numeroDos):
        """
        Parameters:
         - numeroUno
         - numeroDos

        """
        pass

    def Dividir(self, numeroUno, numeroDos):
        """
        Parameters:
         - numeroUno
         - numeroDos

        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def Sumar(self, numeroUno, numeroDos):
        """
        Parameters:
         - numeroUno
         - numeroDos

        """
        self.send_Sumar(numeroUno, numeroDos)
        return self.recv_Sumar()

    def send_Sumar(self, numeroUno, numeroDos):
        self._oprot.writeMessageBegin('Sumar', TMessageType.CALL, self._seqid)
        args = Sumar_args()
        args.numeroUno = numeroUno
        args.numeroDos = numeroDos
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_Sumar(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = Sumar_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "Sumar failed: unknown result")

    def Restar(self, numeroUno, numeroDos):
        """
        Parameters:
         - numeroUno
         - numeroDos

        """
        self.send_Restar(numeroUno, numeroDos)
        return self.recv_Restar()

    def send_Restar(self, numeroUno, numeroDos):
        self._oprot.writeMessageBegin('Restar', TMessageType.CALL, self._seqid)
        args = Restar_args()
        args.numeroUno = numeroUno
        args.numeroDos = numeroDos
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_Restar(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = Restar_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "Restar failed: unknown result")

    def Multiplicar(self, numeroUno, numeroDos):
        """
        Parameters:
         - numeroUno
         - numeroDos

        """
        self.send_Multiplicar(numeroUno, numeroDos)
        return self.recv_Multiplicar()

    def send_Multiplicar(self, numeroUno, numeroDos):
        self._oprot.writeMessageBegin('Multiplicar', TMessageType.CALL, self._seqid)
        args = Multiplicar_args()
        args.numeroUno = numeroUno
        args.numeroDos = numeroDos
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_Multiplicar(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = Multiplicar_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "Multiplicar failed: unknown result")

    def Dividir(self, numeroUno, numeroDos):
        """
        Parameters:
         - numeroUno
         - numeroDos

        """
        self.send_Dividir(numeroUno, numeroDos)
        return self.recv_Dividir()

    def send_Dividir(self, numeroUno, numeroDos):
        self._oprot.writeMessageBegin('Dividir', TMessageType.CALL, self._seqid)
        args = Dividir_args()
        args.numeroUno = numeroUno
        args.numeroDos = numeroDos
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_Dividir(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = Dividir_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "Dividir failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["Sumar"] = Processor.process_Sumar
        self._processMap["Restar"] = Processor.process_Restar
        self._processMap["Multiplicar"] = Processor.process_Multiplicar
        self._processMap["Dividir"] = Processor.process_Dividir
        self._on_message_begin = None

    def on_message_begin(self, func):
        self._on_message_begin = func

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if self._on_message_begin:
            self._on_message_begin(name, type, seqid)
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_Sumar(self, seqid, iprot, oprot):
        args = Sumar_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Sumar_result()
        try:
            result.success = self._handler.Sumar(args.numeroUno, args.numeroDos)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("Sumar", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_Restar(self, seqid, iprot, oprot):
        args = Restar_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Restar_result()
        try:
            result.success = self._handler.Restar(args.numeroUno, args.numeroDos)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("Restar", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_Multiplicar(self, seqid, iprot, oprot):
        args = Multiplicar_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Multiplicar_result()
        try:
            result.success = self._handler.Multiplicar(args.numeroUno, args.numeroDos)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("Multiplicar", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_Dividir(self, seqid, iprot, oprot):
        args = Dividir_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Dividir_result()
        try:
            result.success = self._handler.Dividir(args.numeroUno, args.numeroDos)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("Dividir", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class Sumar_args(object):
    """
    Attributes:
     - numeroUno
     - numeroDos

    """


    def __init__(self, numeroUno=None, numeroDos=None,):
        self.numeroUno = numeroUno
        self.numeroDos = numeroDos

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.DOUBLE:
                    self.numeroUno = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.DOUBLE:
                    self.numeroDos = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Sumar_args')
        if self.numeroUno is not None:
            oprot.writeFieldBegin('numeroUno', TType.DOUBLE, 1)
            oprot.writeDouble(self.numeroUno)
            oprot.writeFieldEnd()
        if self.numeroDos is not None:
            oprot.writeFieldBegin('numeroDos', TType.DOUBLE, 2)
            oprot.writeDouble(self.numeroDos)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(Sumar_args)
Sumar_args.thrift_spec = (
    None,  # 0
    (1, TType.DOUBLE, 'numeroUno', None, None, ),  # 1
    (2, TType.DOUBLE, 'numeroDos', None, None, ),  # 2
)


class Sumar_result(object):
    """
    Attributes:
     - success

    """


    def __init__(self, success=None,):
        self.success = success

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Resultado()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Sumar_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(Sumar_result)
Sumar_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [Resultado, None], None, ),  # 0
)


class Restar_args(object):
    """
    Attributes:
     - numeroUno
     - numeroDos

    """


    def __init__(self, numeroUno=None, numeroDos=None,):
        self.numeroUno = numeroUno
        self.numeroDos = numeroDos

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.DOUBLE:
                    self.numeroUno = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.DOUBLE:
                    self.numeroDos = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Restar_args')
        if self.numeroUno is not None:
            oprot.writeFieldBegin('numeroUno', TType.DOUBLE, 1)
            oprot.writeDouble(self.numeroUno)
            oprot.writeFieldEnd()
        if self.numeroDos is not None:
            oprot.writeFieldBegin('numeroDos', TType.DOUBLE, 2)
            oprot.writeDouble(self.numeroDos)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(Restar_args)
Restar_args.thrift_spec = (
    None,  # 0
    (1, TType.DOUBLE, 'numeroUno', None, None, ),  # 1
    (2, TType.DOUBLE, 'numeroDos', None, None, ),  # 2
)


class Restar_result(object):
    """
    Attributes:
     - success

    """


    def __init__(self, success=None,):
        self.success = success

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Resultado()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Restar_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(Restar_result)
Restar_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [Resultado, None], None, ),  # 0
)


class Multiplicar_args(object):
    """
    Attributes:
     - numeroUno
     - numeroDos

    """


    def __init__(self, numeroUno=None, numeroDos=None,):
        self.numeroUno = numeroUno
        self.numeroDos = numeroDos

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.DOUBLE:
                    self.numeroUno = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.DOUBLE:
                    self.numeroDos = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Multiplicar_args')
        if self.numeroUno is not None:
            oprot.writeFieldBegin('numeroUno', TType.DOUBLE, 1)
            oprot.writeDouble(self.numeroUno)
            oprot.writeFieldEnd()
        if self.numeroDos is not None:
            oprot.writeFieldBegin('numeroDos', TType.DOUBLE, 2)
            oprot.writeDouble(self.numeroDos)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(Multiplicar_args)
Multiplicar_args.thrift_spec = (
    None,  # 0
    (1, TType.DOUBLE, 'numeroUno', None, None, ),  # 1
    (2, TType.DOUBLE, 'numeroDos', None, None, ),  # 2
)


class Multiplicar_result(object):
    """
    Attributes:
     - success

    """


    def __init__(self, success=None,):
        self.success = success

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Resultado()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Multiplicar_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(Multiplicar_result)
Multiplicar_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [Resultado, None], None, ),  # 0
)


class Dividir_args(object):
    """
    Attributes:
     - numeroUno
     - numeroDos

    """


    def __init__(self, numeroUno=None, numeroDos=None,):
        self.numeroUno = numeroUno
        self.numeroDos = numeroDos

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.DOUBLE:
                    self.numeroUno = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.DOUBLE:
                    self.numeroDos = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Dividir_args')
        if self.numeroUno is not None:
            oprot.writeFieldBegin('numeroUno', TType.DOUBLE, 1)
            oprot.writeDouble(self.numeroUno)
            oprot.writeFieldEnd()
        if self.numeroDos is not None:
            oprot.writeFieldBegin('numeroDos', TType.DOUBLE, 2)
            oprot.writeDouble(self.numeroDos)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(Dividir_args)
Dividir_args.thrift_spec = (
    None,  # 0
    (1, TType.DOUBLE, 'numeroUno', None, None, ),  # 1
    (2, TType.DOUBLE, 'numeroDos', None, None, ),  # 2
)


class Dividir_result(object):
    """
    Attributes:
     - success

    """


    def __init__(self, success=None,):
        self.success = success

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Resultado()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Dividir_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(Dividir_result)
Dividir_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [Resultado, None], None, ),  # 0
)
fix_spec(all_structs)
del all_structs

